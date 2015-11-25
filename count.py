a='CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'
b='CGCG'
x=len(b)
count=0
for i in range(len(a)):
    if b==a[i:i+x]:
        count+=1
print count
