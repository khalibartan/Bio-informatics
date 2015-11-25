"""
	Its a problem based on independent alleles..
	Problem goes like this
	at zero generation there is a guy having gene AaBb and he mates 
	with organism with gene AaBb(Actually at all subsequent level 
	of generation tree mating will take place with only this genotype)
	So at every mating two children are born which subsequent mates
	and give two children
	we have to consider AaBb is same to all other 3 combinations having
	genes Aa and Bb which I found quite wierd coz actually they shouldn't
	be same
	so probability of success that is finding a child of type AaBb is 1/4
	and probability of not finding a child of genotype AaBb is 3/4
"""	
"""	
	This problem is reduced to bernoulli trials since alleles are independent
	So this programm is going to be about that
	Bernoulli trials which is following
	Probability(X'success'=r in n total trials)=nCr(p^r)(q^(n-r))
	for at least and atmost we use sum
"""
#Sample inputs
"""
	>>> 2 1
	0.684
	>>> 1 1
	0.4375
"""
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result
def bernoulli(n,r):
	p=1/4
	q=3/4
	pro=binomialCoeff(n,r)*float((p**r))*float((q**(n-r)))
	return pro
k,N=input().split()
k,N=int(k),int(N)
y=2**k
rezult=0
for i in range(N,y+1):
	rezult+=bernoulli(y,i)
print("{0:.3f}".format(rezult))
