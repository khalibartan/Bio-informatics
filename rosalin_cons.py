    import sys
    inputs=sys.stdin.readlines()
    s=''
    l=[]
    for line in inputs:
    	if '>' in line:
    		if len(s)==0:
    			continue
    		else:
    			l.append(s)
    			s=''
    	else:
    		s+=line[:-1]
    x=len(l[0])
    dic={'A':[0 for i in range(x)],'C':[0 for i in range(x)],'G':[0 for i in range(x)],'T':[0 for i in range(x)]}
    y=len(l)
    for j in range(x):
    	for i in range(y):
    		dic[l[i][j]][j]+=1
    for j in range(x):
    	y=max(dic['A'][j],dic['G'][j],dic['C'][j],dic['T'][j])
    	for key in dic:
    		if dic[key][j]==y:
    			print(key,end='')
    			break
    print('\n')
    y=len(dic['A'])
    for key in 'ACGT':
    	print(key+': ',end='')
    	for i in range(y):
    		print(dic[key][i],end=' ')
    	print('\n')


