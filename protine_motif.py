# your code goes here
"""
	So the problem is a motif problem
	inputs are some protiens we have to go to url retrive its fasta format info
	then find the indexes where it has a motif with  N-glycosylation motif
	its motif is given by N{P}[ST]{P} where {X} means all other except X
	and [XY] means one of either X or Y
	fasta format inputs are such a fuss
	I'm going to use regex..helping pepole like me who are lazy 
	[..] will check for any one of the character present in the brackets
	[^..] will check all other characters except those are present in the bracket
"""	
import re
import sys
import urllib
inputs=sys.stdin.readlines()
l=[]
s='http://www.uniprot.org/uniprot/'
x=''
for line in inputs :
	q=s+line.strip()+'.fasta'
	a=urllib.urlopen(q)
	for ll in a.fp:
		if '>' in ll:
			continue
		else:
			x+=ll.strip()
	l=(line.strip(),x)
	x=''
	z=len(l[1])
	count=0
	for i in range(z):
            if re.search(r'N[^P][ST][^P]',l[1][i:i+4]):
			if count==0:
				print l[0]
                                print i+1,
                                count+=1
			else:
				print i+1,
        if count!=0:
            print ''
	l=[]
