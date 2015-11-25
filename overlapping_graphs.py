import sys
inputs=sys.stdin.readlines()
l={}
s=''
for line in inputs:
    if '>' in line:
        try:
            l[key]=s
        except:
            key=line[1:-1]
        key=line[1:-1]
        s=''
        else:
            s+=line.strip()
l[key]=s
from networkx import*
g=graph()


