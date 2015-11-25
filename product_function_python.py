from itertools import product
s=input().replace(' ','')
n=int(input())
for x in product(s, repeat=n):
	w = ''.join(x)
	print(w)
