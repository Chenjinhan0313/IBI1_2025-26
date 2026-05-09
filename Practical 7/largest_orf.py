seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
stop_codons = {'UAA', 'UAG', 'UGA'}
def find_longest_orf(seq):
    max_len = 0
    i = 0
    while i < len(seq) - 2:
        # find the start codon 'AUG'
        if seq[i:i+3] == 'AUG':
            # Scan forward in steps of 3 (one codon) from the start codon
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    # find the stop codons
                    orf_len = j - i + 3
                    if orf_len > max_len:
                        max_len = orf_len
                    break  # the first stop codon is the end of this ORF
        i += 1
    return max_len
longest = find_longest_orf(seq)
print(f"Longest ORF length: {longest} nucleotides")

