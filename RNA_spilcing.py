dic={'TTT':'F','CTT':'L','ATT':'I','GTT':'V',\
'TTC':'F','CTC':'L','ATC':'I','GTC':'V',\
'TTA':'L','CTA':'L','ATA':'I','GTA':'V',\
'TTG':'L','CTG':'L','ATG':'M','GTG':'V',\
'TCT':'S','CCT':'P','ACT':'T','GCT':'A',\
'TCC':'S','CCC':'P','ACC':'T','GCC':'A',\
'TCA':'S','CCA':'P','ACA':'T','GCA':'A',\
'TCG':'S','CCG':'P','ACG':'T','GCG':'A',\
'TAT':'Y','CAT':'H','AAT':'N','GAT':'D',\
'TAC':'Y','CAC':'H','AAC':'N','GAC':'D',\
'CAA':'Q','AAA':'K','GAA':'E',\
'CAG':'Q','AAG':'K','GAG':'E',\
'TGT':'C','CGT':'R','AGT':'S','GGT':'G',\
'TGC':'C','CGC':'R','AGC':'S','GGC':'G',\
'CGA':'R','AGA':'R','GGA':'G',\
'TGG':'W','CGG':'R','AGG':'R','GGG':'G'}
import sys
inputs=sys.stdin.readlines()
l=[]
s=''
for line in inputs:
    if '>' in line:
        if s!='':	
            l.append(s)
            s=''
    else:
        s+=line.strip()
l.append(s)
dna=l[0]
l.remove(dna)
x=len(dna)
for i in range(x):
    for key in l:
        y=len(key)
            if key==dna[i:i+y]:
                dna=dna[:i]+dna[i+y:]
                    i+=y-2
                    break
x=len(dna)-3
s=''
for i in range(0,x,3):
    s+=dic[dna[i:i+3]]
print(s)


