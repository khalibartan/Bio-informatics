    # your code goes here
    """
    	signed permutations
    	I'm going to use function permutation
    	first i'm going to take a list of number
    	then make a negative of each number
    	then append them in alist
    """
    fout=open('abc.txt','w')
    from itertools import permutations
    z=int(input())
    a=[i for i in range(1,z+1)]
    b=[-i for i in a]
    for i in b:
    	a.append(i)
    b=[]
    for x in permutations(a,z):
    	flag=0
    	for y in x:
    		w=(-1)*y
    		if w in x:
    			flag=1
    			break
    	if flag==0:
    		w=''
    		for ch in x:
    			w+=str(ch)+' '
    		b.append(w)
    x=str(len(b))+'\n'
    fout.write(x)
    for x in b:
    	x+='\n'
    	fout.write(x)
     


