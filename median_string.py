from d_neighbours import Neighbours,HammingDistance
from sys import stdin as st
inputs=st.readlines()
k=inputs[0].strip()
k=int(k)
del inputs[0]
possible_k_mers=[]
for line in inputs:
    line=line.strip()
    for i in range(len(line)-k+1):
        possible_k_mers.extend(list(Neighbours(line[i:i+k],k)))
k_mers=dict([(k_mer,0) for k_mer in possible_k_mers])
del possible_k_mers
Median=k*len(inputs)
mo=[]
for k_mer in k_mers:
    summ=0
    for line in inputs:
        line=line.strip()
        hamming=k
        for i in range(len(line)-k+1):
            d=HammingDistance(k_mer,line[i:i+k])
            if hamming>d:
                hamming=d
        summ+=hamming
    if Median>summ:
        Median=summ
        mo=[k_mer]
    elif Median==summ:
        mo.append(k_mer)
print mo
