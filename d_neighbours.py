def Neighbours(pattern,d):
    if d==0:
        return pattern
    if len(pattern)==1:
        return {'A','C','G','T'}
    Neighborhood=set()
    total_neighbours=set()
    SuffixNeighbors=Neighbours(pattern[1:],d)
    for x in SuffixNeighbors:
        if HammingDistance(pattern[1:],x)<d:
            for z in 'ACGT':
                Neighborhood.add(z+x)
        else:
            Neighborhood.add(pattern[0]+x)
    return Neighborhood

def HammingDistance(pattern1,pattern2):
    cn=0
    for u in range(len(pattern1)):
        if pattern1[u]!=pattern2[u]:
            cn+=1
    return cn

def reverse_compliment(dna):
    s=''
    dic={'A':'T','T':'A','C':'G','G':'C'}
    for i in reversed(range(len(dna))):
        s+=dic[dna[i]]
    return s

if __name__ == "__main__":
    text=raw_input()
    k,d=raw_input().split()
    k,d=int(k),int(d)
    possible_k_mers=[]
    y=len(text)-k+1
    maxi=0
    for i in range(y):
        possible_k_mers.extend(list(Neighbours(text[i:i+k],d)))
    count_k_mer_frequency=dict([(k_mer,0) for k_mer in possible_k_mers])
    for k_mer in possible_k_mers:
        reverse_mer=reverse_compliment(k_mer)
        count_k_mer_frequency[reverse_mer]=0
    for i in range(y):
        for k_mer in Neighbours(text[i:i+k],d):
            count_k_mer_frequency[k_mer]+=1
    for k_mer in possible_k_mers:
        reverse_mer=reverse_compliment(k_mer)
        count_k_mer_frequency[k_mer]+=count_k_mer_frequency[reverse_mer]
        count_k_mer_frequency[reverse_mer]=count_k_mer_frequency[k_mer]

    max_frequency=max(count_k_mer_frequency.values())
    frequent_words=[]
    for k_mer in count_k_mer_frequency:
            if count_k_mer_frequency[k_mer]==max_frequency:
                frequent_words.append(k_mer)
    for key in frequent_words:
        print key,

