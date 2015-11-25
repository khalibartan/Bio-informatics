from greedy_motif_search import score,profile,profile_most_probable_kmer
from random import randint
def RandomMotifSearch(Dna,k,t):
    random_motifs=[]
    length=len(Dna[0])-k+1
    for line in Dna:
        x=randint(0,length)
        random_motifs.append(line[x:x+k])
    best_score=score(random_motifs)
    temp=[]
    temp.extend(random_motifs)
    while(True):
        motifs=[]
        for line in Dna :
            current_profile=profile(temp)
            x=profile_most_probable_kmer(line,k,current_profile)
            temp.append(x)
            motifs.append(x)
        x=score(motifs)
        if x<best_score :
            best_motifs=[]
            best_motifs.extend(motifs)
            best_score=x
            temp=[]
            temp.extend(best_motifs)
        else:
            return best_motifs,x
def main():
    with open('in.txt') as input_data:
        k, t = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data]
    b_score=k*t
    a=0
    while a!=1000:
        new_motif,new_score=RandomMotifSearch(dna_list,k,t)
        if new_score<b_score:
            b_score=new_score
            best_motif=new_motif
            del new_motif
        a+=1
    print b_score
    with open('out.txt', 'w') as output_data:
        output_data.write('\n'.join(best_motif))

if __name__=='__main__':
    main()
