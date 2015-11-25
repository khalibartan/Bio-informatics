fout=open('rezult.txt','w')
b=int(input())
a=[i for i in range(1,b+1)]
import itertools
x=list(itertools.permutations(a))
fout.write(str(len(x))+'\n')
for li in x:
    for ch in li:
        fout.write(str(ch)+' ')
    fout.write('\n')


