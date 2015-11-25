a=input().split()
from math import factorial
a=[int(i) for i in a]
a[1]=a[0]-a[1]
product=1
while(a[0]!=a[1]):
	product=((product%1000000)*(a[0]%1000000))%1000000
	a[0]-=1
print(product)
