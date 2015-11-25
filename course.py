a='TGCA'
from itertools import product
summ=0
for x in product(a,repeat=4):
    w=''.join(x)
    count=0
    for i in range(4):
        if w[i]!=a[i]:
            count+=1
    if count<=3:
        summ+=1
print summ

