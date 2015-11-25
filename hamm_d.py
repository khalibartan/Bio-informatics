a=raw_input()
b=raw_input()
d=int(raw_input())
x=len(b)
summ=0
for i in range(len(a)-x+1):
    s=a[i:i+x]
    count=0
    for j in range(x):
        if s[j]!=b[j]:
            count+=1
    if count<=d:
        summ+=1
        #print i,
print summ

