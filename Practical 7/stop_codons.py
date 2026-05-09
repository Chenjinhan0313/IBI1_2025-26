import re
def find_stop_codons_in_longest_ORF(seq):
    #Define the three stop codons as a set for O(1) lookup
    stop_codons={'TAA','TAG','TGA'}
    #Track the longest ORF length and the stop codons found in it
    longest_orf_length = 0
    stop_codons_in_longest = []
    # Scan through the entire sequence to find all possible start codons
    # Loop until len(seq)-3 
    for start_pos in range(len(seq) - 2):
        if seq[start_pos:start_pos+3] == 'ATG':
            # Scan forward in steps of 3 (codon by codon)
            # Start from the start codon position
            for j in range(start_pos, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    # Calculate ORF length (from start to end of stop codon)
                    orf_length = j - start_pos + 3
                    if orf_length > longest_orf_length:
                        longest_orf_length = orf_length
                        stop_codons_in_longest = [codon]# Start new list with this stop codon
                    elif orf_length == longest_orf_length:
                        if codon not in stop_codons_in_longest:
                            stop_codons_in_longest.append(codon)
                    # Stop scanning this ORF (first stop codon encountered)
                    break
# Return sorted unique stop codons (set ensures uniqueness)
    return sorted(set(stop_codons_in_longest))
# Open input FASTA file for reading and output file for writing                       
with open('Practical 7/yeast.fa', 'r') as f_in, open('Practical 7/stop_genes.fa', 'w') as f_out:
    current_gene_name = None
    current_seq_lines = []
    for line in f_in:
        line = line.rstrip() #remove newline character
        #check if this is a header line (start with '>')
        if re.search(r'^>',line):
            if current_gene_name is not None and current_seq_lines:
                seq = ''.join(current_seq_lines)
                stops = find_stop_codons_in_longest_ORF(seq)
                if stops:
                    f_out.write(f'>{current_gene_name} {" ".join(stops)}\n')
                    f_out.write(seq + '\n')
            
                for i in current_seq_lines:
                    seq+=i
                stops=[]
                start=seq.find('ATG')
                for i in range(start, len(seq)-2, 3):
                    codon = seq[i:i+3]
                    if codon in ['TAA', 'TAG', 'TGA']:
                        stops.append(codon)
                if stops:
                    f_out.write(f'>{current_gene_name} {" ".join(sorted(stops))}\n')
                    f_out.write(seq + '\n')
            match = re.search(r'gene:(\S+)', line)
            if match:
                current_gene_name = match.group(1)
            else:
                current_gene_name=line[1:].split()[0]
            #reset sequence lines for the new gene
            current_seq_lines = []
        else:
            if line:
                current_seq_lines.append(line)
    #handle the last gene in the file (after the loop ends)
    if current_gene_name is not None and current_seq_lines:
        seq = ''.join(current_seq_lines)
        stops = find_stop_codons_in_longest_ORF(seq)
        if stops:
            f_out.write(f'>{current_gene_name} {" ".join(stops)}\n')
            f_out.write(seq + '\n')
print("Done! Output shwon in stop_genes.fa")
