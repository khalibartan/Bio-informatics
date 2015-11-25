def skew(s):
    flag=1
    count=0
    for i in range(len(s)):
        if s[i]=='G':
            if flag==0:
                vals.append(count)
                valss.append((i,count))
            flag=1
            count+=1
        elif s[i]=='C':
            flag=0
            count-=1
        elif flag==0:
            vals.append(count)
            valss.append((i,count))
vals=[]
valss=[]
skew(raw_input())
mini=min(vals)
for i in range(len(valss)):
    if valss[i][1]==mini:
        print valss[i][0],
print ''
