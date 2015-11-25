dic={'M':1,'A':4,'C':2,'F':2,'L':6,'I':3,'V':4,'S':6,'P':4,'T':4,'Y':2,'H':2,'N':2,'D':2,'Q':2,'K':2,'E':2,'R':6,'G':4,'W':1}
a=input()
a=a.strip()
rezult=1
for char in a:
	rezult=((dic[char]%1000000)*(rezult%1000000))%1000000
rezult=(rezult*3)%1000000
print(rezult)
