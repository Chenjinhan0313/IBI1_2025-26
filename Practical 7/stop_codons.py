import re
with open('Practical 7/yeast.fa', 'r') as f_in, open('Practical 7/stop_genes.fa', 'w') as f_out:
    current_gene_name = None
    current_seq_lines = []
    for line in f_in:
        line = line.rstrip() #remove newline character
        #check if this is a header line (start with '>')
        if re.search(r'^>',line):
            if current_gene_name is not None and current_seq_lines:
                seq = ''.join(current_seq_lines)
                # Find which stop codons appear at least once in the sequence
                stops = []
                if 'TAA' in seq:
                    stops.append('TAA')
                if 'TAG' in seq:
                    stops.append('TAG')
                if 'TGA' in seq:
                    stops.append('TGA')
                if stops:
                    f_out.write(f'>{current_gene_name} {" ".join(stops)}\n')
                    f_out.write(seq + '\n')
            # Extract gene name from header line
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
        stops = []
        if 'TAA' in seq:
                    stops.append('TAA')
        if 'TAG' in seq:
                    stops.append('TAG')
        if 'TGA' in seq:
                    stops.append('TGA')
        if stops:
            f_out.write(f'>{current_gene_name} {" ".join(stops)}\n')
            f_out.write(seq + '\n')
print("Done! Output shwon in stop_genes.fa")
