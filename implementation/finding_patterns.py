from collections import defaultdict

def frequent_kmers_for_clumps(genome, k_mer_size, threshold_count, k_mer_dict, clump_set):

    for i in range(len(genome) - k_mer_size + 1):

        k_mer = genome[i:i+k_mer_size]
        k_mer_dict[k_mer] += 1

        if k_mer_dict[k_mer] == threshold_count:
            clump_set.add(k_mer)

            
def find_clumps(genome, k_mer_size, window_size, threshold_count):

    k_mers = defaultdict(int)
    clump_set = set() # to keep track of k-mers that have reached a threshold count

    frequent_kmers_for_clumps(genome[:window_size], k_mer_size, threshold_count, k_mers, clump_set)
    
    for i in range(1, len(genome) - window_size + 1):

        first_kmer = genome[i - 1: i - 1 + k_mer_size] # before moving to the next window, we want to subtract one
                                                       # occurence of the very first k_mer
        k_mers[first_kmer] -= 1

        if k_mers[first_kmer] == 0:
            del k_mers[first_kmer]

        new_window = genome[i + window_size - k_mer_size:i + window_size]
        frequent_kmers_for_clumps(new_window, k_mer_size, threshold_count, k_mers, clump_set)

    return ' '.join(elem for elem in clump_set)

def hamming_distance(string1, string2):
    
    if len(string1) != len(string2):
        return ValueError("Strings must be of the same length to compute Hamming distance.")
    
    return sum(1 for i in range(len(string1)) if string1[i] != string2[i])

def generate_neighborhood(string, num_mismatch):
    nucleotides = ['A', 'G', 'T', 'C']
    
    if(num_mismatch == 0):
        return string
    
    elif(len(string) == 1):
        return {'A', 'G', 'C', 'T'}
    
    else:
        neighborhood = set()

        suffix = generate_neighborhood(string[1:], num_mismatch)

        for i in suffix:
            if hamming_distance(string[1:], i) < num_mismatch:
                for j in nucleotides:
                    neighborhood.add(j + i)
            else:
                neighborhood.add(string[0] + i)

        return neighborhood
