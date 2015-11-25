# your code goes here
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

N,pr=raw_input().split()
N,pr=int(N),float(pr)
a=raw_input()
countAT=0
countGC=0
for char in a:
    if char=='A' or char=='T':
        countAT+=1
    else:
        countGC+=1
gc=pr/2.0
at=(1-pr)/2.0
p=(gc**countGC)*(at**countAT)
q=1-p
rezult=1-q**N
print "{0:.3f}".format(rezult)


