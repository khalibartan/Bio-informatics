import sys
inputs=sys.stdin.readlines()
imp=''
for line in inputs:
	if '>' in line:
		continue
	else:
		imp+=line.strip()
inputs=len(imp)
sub_strings={}
l=[]
for i in range(inputs):
	for j in range(i+4,i+13):
		sub_strings[imp[i:j]]=1
 
for key in sub_strings:
	if len(key)<4:
		continue
	reverse_compliment=''
	x=len(key)
	for i in reversed(range(x)):
		if key[i]=='A':
			reverse_compliment+='T'
		elif key[i]=='T':
			reverse_compliment+='A'
		elif key[i]=='G':
			reverse_compliment+='C'
		elif key[i]=='C':
			reverse_compliment+='G'
	if reverse_compliment==key:
		l.append(key)
for key in l:
	for i in range(inputs):
		x=len(key)
		if key in imp[i:i+x]:
			print(i+1,x)
