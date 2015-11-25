    dic={'TTT':'F','CTT':'L','ATT':'I','GTT':'V',\
    'TTC':'F','CTC':'L','ATC':'I','GTC':'V',\
    'TTA':'L','CTA':'L','ATA':'I','GTA':'V',\
    'TTG':'L','CTG':'L','ATG':'M','GTG':'V',\
    'TCT':'S','CCT':'P','ACT':'T','GCT':'A',\
    'TCC':'S','CCC':'P','ACC':'T','GCC':'A',\
    'TCA':'S','CCA':'P','ACA':'T','GCA':'A',\
    'TCG':'S','CCG':'P','ACG':'T','GCG':'A',\
    'TAT':'Y','CAT':'H','AAT':'N','GAT':'D',\
    'TAC':'Y','CAC':'H','AAC':'N','GAC':'D',\
    'CAA':'Q','AAA':'K','GAA':'E',\
    'CAG':'Q','AAG':'K','GAG':'E',\
    'TGT':'C','CGT':'R','AGT':'S','GGT':'G',\
    'TGC':'C','CGC':'R','AGC':'S','GGC':'G',\
    'CGA':'R','AGA':'R','GGA':'G',\
    'TGG':'W','CGG':'R','AGG':'R','GGG':'G'}
    import sys
    inputs=sys.stdin.readlines()
    imp=''
    for line in inputs:
    	if '>' in line:
    		continue
    	else:
    		imp+=line.strip()
    inputs=imp
    x=len(inputs)
    imp=''
    for i in reversed(range(x)):
    	if inputs[i]=='A':
    		imp+='T'
    	elif inputs[i]=='T':
    		imp+='A'
    	elif inputs[i]=='G':
    		imp+='C'
    	elif inputs[i]=='C':
    		imp+='G'
    di={}
    for i in range(x):
    	if inputs[i:i+3]=='ATG':
    		s=''
    		for j in range(i,x,3):
    			if inputs[j:j+3]=='TAG' or inputs[j:j+3]=='TGA' or inputs[j:j+3]=='TAA':
    				if di.get(s,0)==0:
    					di[s]=1
    					print(s)
    					break
    				else:
    					break
    			else:
    				s+=dic[inputs[j:j+3]]
    for i in range(x):
    	if imp[i:i+3]=='ATG':
    		s=''
    		for j in range(i,x,3):
    			if imp[j:j+3]=='TAG' or imp[j:j+3]=='TGA' or imp[j:j+3]=='TAA':
    				if di.get(s,0)==0:
    					di[s]=1
    					print(s)
    					break
    				else:
    					break
    			else:
    				s+=dic[imp[j:j+3]]
     
