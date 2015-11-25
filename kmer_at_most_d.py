a=raw_input()
b=raw_input()
d=int(raw_input())
x=len(a)
summ=0
for i in range(len(b)-x+1):
    s=b[i:i+x]
    count=0
    for j in range(x):
        if s[j]!=a[j]:
            count+=1
    if count<=d:
        summ+=1
        #print i,
print summ


