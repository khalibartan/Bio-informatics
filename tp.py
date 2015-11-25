from greedy_motif_search import score,profile,profile_most_probable_kmer
motifs=[]
Dna=['AAGCCAAA','AATCCTGG','GCTACTTG','ATGTTTTG']
temp=['CCA','CCT','CTT','TTG']
for line in Dna :
    current_profile=profile(temp)
    x=profile_most_probable_kmer(line,3,current_profile)
    temp.append(x)
    motifs.append(x)
print ' '.join(motifs)

