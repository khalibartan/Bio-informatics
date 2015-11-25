def longest_inc(D):
    x=len(D)
    inc=[list() for i in range(x)]
    inc[0].append(D[0])
    for i in range(1,x):
        for j in range(i):
 # l.append(max() + [d[i]])
 # [l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len
            if (D[j]<D[i]) and (len(inc[i])<len(inc[j])+1):
                inc[i]=list()
                inc[i].extend(inc[j])
        inc[i].append(D[i])
    return inc

def longest_dic(D):
    x=len(D)
    dec=[list() for i in range(x)]
    dec[0].append(D[0])
    for i in range(1,x):
        for j in range(i):
            if (D[j]>D[i]) and (len(dec[i])<len(dec[j])+1):
                dec[i]=list()
                dec[i].extend(dec[j])
        dec[i].append(D[i])
    return dec

a=raw_input()
a=raw_input().split()
a=[int(i) for i in a]
i,d=longest_inc(a), longest_dic(a)
inci=0
deci=0
for j in range(len(i)):
    if  len(i[j])>len(i[inci]):
        inci=j
for j in range(len(d)):
    if  len(d[j])>len(d[deci]):
        deci=j
for j in i[inci]:
    print j,
print ''
for j in d[deci]:
    print j,



