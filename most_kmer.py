a='CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA'
dic={}
for i in range(len(a)):
    dic[a[i:i+3]]=dic.get(a[i:i+3],0)+1
maxs,maxv='CGG',dic['CGG']
for key in dic:
    print key,dic[key]
    if dic[key]>maxv:
        maxs,maxv=key,dic[key]
print maxs
