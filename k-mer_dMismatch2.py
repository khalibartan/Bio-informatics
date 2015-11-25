a=raw_input()
k,d=raw_input().split()
k,d=int(k),int(d)
from itertools import product
dic={}
l=[]
maxi=0
for x in product('ATGC',repeat=k):
    key=''.join(x)
    count=0
    for j in range(len(a)-k):
        x=a[j:j+k]
        countd=0
        for y in range(k):
            if x[y]!=key[y]:
                countd+=1
        if countd<=d:
            count+=1
    if maxi==count:
        l.append(key)
    elif maxi<count:
        maxi=count
        del l
        l=[]
        l.append(key)
for key in l:
    print key,


