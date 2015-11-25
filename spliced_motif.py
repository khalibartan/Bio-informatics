def lcs(xstr, ystr):
    a=xstr+','+ystr
    if dic.get(a,0)!=0:
        return dic[a]
    if not xstr or not ystr:
            return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        a=xs+','+ys
        dic[a]=lcs(xs,ys)
        return x + dic[a]
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)
import sys
inputs=sys.stdin.readlines()
l=[]
dic={}
s=''
for line in inputs:
    if '>' in line:
        if s!='':
            l.append(s)
            s=''
    else:
        s+=line.strip()
l.append(s)
print lcs(l[0],l[1])
