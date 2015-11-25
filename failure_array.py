import sys
inputs=sys.stdin.readlines()
s=''
for line in inputs:
    if '>' in line:
        continue
    else:
        s+=line.strip()
p=[0 for i in range(len(s))]
for k in range(len(s)):
    x=[]
    for j in range(1,k):
        a=s[j:k]
        if a==s[:k-j]:
            x.append(len(a))
        if len(x)!=0:
            p[k]=max(x)
for i in p:
    print i,
