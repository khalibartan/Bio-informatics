n=int(input())
m=int(input())
A=input().split()
s=input().split()
A=[int(i) for i in A]
s=[int(i) for i in s]

for el in s:
	low=0
	high=len(A)-1
	flag=0
	while(low<=high):
		mid=int((low+high)/2)
		if el<A[mid]:
			high=mid-1
		elif el>A[mid]:
			low=mid+1
		else:
			flag=1
			print mid+1,
			break
	if flag==0:
		print'-1',
print ''
