# your code goes here
import sys
inputs=sys.stdin.readlines()
l=[]
s=''
for line in inputs:
	if '>' in line:
		l.append(s)
		s=''
	else:
		s+=line.strip()
l.append(s)
s=zip(l[0],l[1])
del l
transition=0
traversion=0
print(s)
for s1,s2 in s:
	if s1=='A' and s2=='G' :
		transition+=1
	elif s1=='G' and s2=='A':
		transition+=1	
	elif s1=='T' and s2=='C':
		transition+=1	
	elif s1=='C' and s2=='T':
		transition+=1
	else:
		traversion+=1
l=transition/traversion
print(l)
