from greedy_motif_search import score
from random import randint
import numpy as np
import sympy as sp

def special_profile(k_mers,k):
    dic=dict()
    dic={'A':[1 for i in range(k)],'C':[1 for i in range(k)],'G':[1 for i in range(k)],'T':[1 for i in range(k)]}
    for motif in k_mers:
        for i,char in enumerate(motif):
            dic[char][i]+=1
    return dic

def biased_random_kmer(profile,dna,k):
    probability_of_kmers=[]
    k_mers=[]
    for i in range(len(dna)-k+1):
        pr=1.0
        for j,char in enumerate(dna[i:i+k]):
            pr*=profile[char][j]
        probability_of_kmers.append(pr)
        k_mers.append(dna[i:i+k])
    divisor=sum(probability_of_kmers)
    probability_of_kmers = [float(pr)/divisor for pr in probability_of_kmers]
    return np.random.choice(k_mers,1,p=probability_of_kmers)

def GibbsSampler(Dna,k,t,N):
    random_motifs=[]
    length=len(Dna[0])-k
    for line in Dna:
        i=randint(0,length)
        random_motifs.append(line[i:i+k])
    best_score=score(random_motifs)
    best_motifs=[]
    best_motifs.extend(random_motifs)
    for x in range(N):
        i=randint(0,t-1)
        current_profile=special_profile(best_motifs[:i]+best_motifs[i+1:],k)
        a=list(biased_random_kmer(current_profile,Dna[i],k))
        motifs=[]
        motifs.extend(best_motifs[:i]+a+best_motifs[i+1:])
        if score(motifs)<best_score:
            best_motifs=[]
            best_motifs.extend(motifs)
            best_score=score(best_motifs)
    return best_motifs,best_score

def main():
    with open('in.txt') as input_data:
        k, t,N = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data]
    # best_motif,best_score = GibbsSampler(dna_list, k, t,N)
    motif_score = [GibbsSampler(dna_list, k, t, N) for i in range(20)]
    motifs = [motif for motif, score in motif_score]
    score = np.array([score for motif, score in motif_score])
    best_score = min(score)
    best_motif = motifs[best_score.argmin()]
    print best_score
    with open('out.txt', 'w') as output_data:
        output_data.write('\n'.join(best_motif))

if __name__=='__main__':
    main()
