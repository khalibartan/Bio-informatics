# your code goes here
n,m=raw_input().split()
n,m=int(n),int(m)
count=[0 for i in range(n)]
inputs=[]
for i in range(m):
	s=raw_input().split()
	s=[int(j) for j in s]
	count[s[0]-1]+=1
	count[s[1]-1]+=1
for x in count:
	print x,
print('')
