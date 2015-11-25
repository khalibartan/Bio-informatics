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
    l.remove('')
    transition=0
    traversion=0
    for i in range(len(l[0])):
    	if l[0][i]=='A' and l[1][i]=='G' :
    		transition+=1
    	elif l[0][i]=='G' and l[1][i]=='A':
    		transition+=1	
    	elif l[0][i]=='T' and l[1][i]=='C':
    		transition+=1	
    	elif l[0][i]=='C' and l[1][i]=='T':
    		transition+=1
    	elif l[0][i]==l[1][i]:
    		continue
    	else:
    		traversion+=1
    l=transition/traversion
    print("{0:.11f}".format(l))


