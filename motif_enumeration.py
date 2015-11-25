def Neighbours(pattern,d):
    if d==0:
        return pattern
    if len(pattern)==1:
        return {'A','C','G','T'}
    Neighborhood=set()
    total_neighbours=set()
    SuffixNeighbors=Neighbours(pattern[1:],d)
    for x in SuffixNeighbors:
        if HammingDistance(pattern[1:],x)<d:
            for z in 'ACGT':
                Neighborhood.add(z+x)
        else:
            Neighborhood.add(pattern[0]+x)
    return Neighborhood

def HammingDistance(pattern1,pattern2):
    cn=0
    for u in range(len(pattern1)):
        if pattern1[u]!=pattern2[u]:
            cn+=1
    return cn

import sys
inputs=sys.stdin.readlines()
a=inputs[0]
a=a.strip()
k,d=a.split()
k,d=int(k),int(d)
del inputs[0]

possible_k_mers=[]

for line in inputs:
    line=line.strip()
    for i in range(len(line)-k+1):
        possible_k_mers.extend(list(Neighbours(line[i:i+k],d)))

count_k_mer=dict([(k_mer,dict()) for k_mer in possible_k_mers])

line_list={}
for i,line in enumerate(inputs):
    line=line.strip()
    line_list[i]=1
    for j in range(len(line)-k+1):
        for k_mer in Neighbours(line[j:j+k],d):
            count_k_mer[k_mer][i]=1

for k_mer in count_k_mer:
    if count_k_mer[k_mer]==line_list:
        print k_mer,

