# your code goes here
string=raw_input()
string=string.replace(' ','')
n=int(raw_input())
s=''
dic={}
L=[]
for i,key in enumerate(string):
	dic[i]=key
	L.append(i)
l=[]
from itertools import product
for i in range(1,n+1):
	for x in product(L,repeat=i):
		l.append(x)
l.sort()
s=''
for st in l:
	for ch in st:
		s+=string[ch]
	print s
	s=''
	
