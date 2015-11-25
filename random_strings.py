import math
a=input()
A=input().split(' ')
A=[float(i) for i in A]
countAT=0
countGC=0
B=[]
for char in a:
	if char=='A' or char=='T':
		countAT+=1
	else:
		countGC+=1
for pro in A:
	gc=pro/2.0
	at=(1-pro)/2.0
	c=(countAT*(math.log(at,10)))+(countGC*(math.log(gc,10)))
	B.append(c)
for c in B:
	print("{0:.3f}".format(c),end=' ')
print('')
