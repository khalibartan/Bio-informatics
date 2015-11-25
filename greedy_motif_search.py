def profile_most_probable_kmer(dna, k, profile):
    '''Returns the profile most probable k-mer for the given input data.'''
    # A dictionary relating nucleotides to their position within the profile.
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # Initialize the maximum probabily.
    max_probability = -1

    # Compute the probability of the each k-mer, store it if it's currently a maximum.
    for i in xrange(len(dna)-k+1):
        # Get the current probability.
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            try:
                current_probability *= profile[j][nuc_loc[nucleotide]]
            except:
                break
        # Check for a maximum.
        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable
def score(motifs):
    '''Returns the score of the given list of motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile(motifs):
    '''Returns the profile of the dna list motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)+1) / float(len(col)+1) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search(dna_list, k, t):
    '''Runs the Greedy Motif Search algorithm and retuns the best motif.'''
    # Initialize the best score as a score higher than the highest possible score.
    best_score = t*k

    # Run the greedy motif search.
    for i in xrange(len(dna_list[0])-k+1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [dna_list[0][i:i+k]]

        # Find the most probable k-mer in the next string.
        for j in xrange(1, t):
            current_profile = profile(motifs)
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))

        # Check to see if we have a new best scoring list of motifs.
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs
def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('in.txt') as input_data:
        k, t = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data]

    # Run the Greedy Motif Search.
    best_motifs = greedy_motif_search(dna_list, k, t)

    # Print and save the answer.
    print score(best_motifs)
    print profile(best_motifs)
    with open('out.txt', 'w') as output_data:
        output_data.write('\n'.join(best_motifs))

if __name__ == '__main__':
    main()
