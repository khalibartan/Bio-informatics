from sys import stdin as st
inputs=st.readlines()
s=inputs[0].strip()
k=int(inputs[1].strip())
del inputs[0]
del inputs[0]
dic={'A':[],'C':[],'G':[],'T':[]}
for i,line in enumerate(inputs) :
    line=line.strip()
    if i==0:
        dic['A']=line.split()
        dic['A']=[float(i) for i in dic['A']]
    elif i==1:
        dic['C']=line.split()
        dic['C']=[float(i) for i in dic['C']]
    elif i==2:
        dic['G']=line.split()
        dic['G']=[float(i) for i in dic['G']]
    elif i==3:
        dic['T']=line.split()
        dic['T']=[float(i) for i in dic['T']]
max_probability=0
for i in range(len(s)-k+1):
    a=s[i:i+k]
    pr=1
    for x,char in enumerate(a):
        pr*=dic[char][x]
    if pr>max_probability:
        max_probability=pr
        max_pr_k_mer=a
print max_pr_k_mer
