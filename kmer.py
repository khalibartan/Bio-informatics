import sys
inputs=sys.stdin.readlines()
for line in inputs:
    if '>' in line:
        s=''
    else:
        s+=line.strip()
l=[]
from itertools import product
for x in product('ACGT',repeat=4):
    w=''.join(x)
    count =0
    for i in range(len(s)):
        if w in s[i:i+4]:
            count+=1
    l.append((w,count))
for i in range(len(l)):
    print l[i][1],
print''

