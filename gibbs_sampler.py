from random import randint
from operator import ne
def HammingDistance(seq1, seq2):
    'Returns the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(map(ne, seq1, seq2))
def score(motifs):
	'''Returns the score of the dna list motifs.'''
	score = 0
	for i in xrange(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		score += min([HammingDistance(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
	return score
def profile_with_pseudocounts(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc)+1)/float(len(col)+4) for nuc in 'ACGT'])
	return prof
def profile_most_probable_kmer(dna, k, prof):
	'''Return the profile most probable k-mer in a given dna sequence.'''
	# A dictionary relating nucleotides to their position within the profile.
	nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
	# Initialize the maximum probabily.
	max_prob = [-1, None]
	# Compute the probability of the each k-mer, store it if it's currently a maximum.
	for i in xrange(len(dna)-k+1):
		current_prob = 1
		for j, nucleotide in enumerate(dna[i:i+k]):
			current_prob *= prof[j][nuc_loc[nucleotide]]
		if current_prob > max_prob[0]:
			max_prob = [current_prob, dna[i:i+k]]

	return max_prob[1]
def profile(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc))/float(len(col)) for nuc in 'ACGT'])
	return prof
def gibbs_sampler(dna,k,t,N):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in xrange(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]

	# Iterate motifs.
	for i in xrange(N):
		r = randint(0,t-1)
		current_profile = profile_with_pseudocounts([motif for index, motif in enumerate(motifs) if index!=r])
		# print 'a: ', motifs
		motifs = [profile_most_probable_kmer(dna[index],k,current_profile) if index == r else motif for index,motif in enumerate(motifs)]
		# print 'b: ', motifs
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	return best_score

if __name__ == '__main__':

	with open('in.txt') as input_data:
		k,t,N = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best scoring motifs as a score higher than the highest possible score.
	best_motifs = [k*t, None]

	# Repeat the radomized motif search 20 times.
	for repeat in xrange(20):
		current_motifs = gibbs_sampler(dna_list,k,t,N)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs

	# Print and save the answer.
	print score(best_motifs)
	with open('out.txt', 'w') as output_data:
		output_data.write('\n'.join(best_motifs[1]))
