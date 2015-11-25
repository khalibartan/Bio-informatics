# your code goes here
#Motif problem
# Motif is defined as a pattern which is repeated in given various amino acids
"""
	Algorithm description:
	First make a list of all substring of first amino acid
	then chose a random selected amino acid compare the 
	list of substring with the selected amino acid
	remove the substrings which do not match
	repeat above process may in a random order or not
	Random amino acid is choosen because to reduce 
	the number of similar substring
	PS:I'm not gonna apply random method because i don't know a efficent way 
	to chose a random number which has not been choseen already
	instead it is better to apply normal method
"""
"""
	sample input and outputs
	>>> Rosalind_1
		GATTACA
		>Rosalind_2
		TAGACCA
		>Rosalind_3
		ATACA
	AC
"""
"""	rm is a remove function which deletes the strings which 
	will not occur because a its substring is not present
"""
def motifing(index):
	q=[]
	global sub_strings
	global l
	for key in sub_strings:
		if key not in l[index]:
			q.append(key)
	for key in q:
		 del sub_strings[key]
import sys
ip=sys.stdin.readlines()
s=''
l=[]
for line in ip:
	if '>' in line:
		if len(s)==0:
			continue
		else:
			l.append(s)
			s=''
	else:
		s+=line[:-1]
k=len(l)
x=l[0]
y=len(x)
sub_strings={}
for i in range(y):
	for j in range(i+1,y):
		sub_strings[x[i:j]]=1
for j in range(1,k):
	motifing(j)
for key in sub_strings:
	k=[key,len(key)]
	break
for key in sub_strings:
	if len(key)>k[1]:
		k=[key,len(key)]
print(k[0])

