import re
with open('Practical 7/yeast.fa', 'r') as f_in, open('Practical 7/stop_genes.fa', 'w') as f_out:
    current_gene = None
    current_seq = []
    for line in f_in:
        line = line.rstrip()
        if re.search(r'^>',line):
            if current_gene and current_seq:
                seq = ''
                for i in current_seq:
                    seq+=i
                stops=[]
                start=seq.find('ATG')
                for i in range(start, len(seq)-2, 3):
                    codon = seq[i:i+3]
                    if codon in ['TAA', 'TAG', 'TGA']:
                        stops.append(codon)
                if stops:
                    f_out.write(f'>{current_gene} {" ".join(sorted(stops))}\n')
                    f_out.write(seq + '\n')
            match = re.search(r'gene:(\S+)', line)
            if match:
                current_gene = match.group(1)
            current_seq = []
        else:
            if line:
                current_seq.append(line)
    if current_gene and current_seq:
        seq = ''.join(current_seq)
        stops = []
        match=re.search(r'ATG',seq)
        if match:
            start = match.start()
        else:
            start=-1
        if start != -1:
            for i in range(start, len(seq)-2, 3):
                codon = seq[i:i+3]
                if codon in ['TAA', 'TAG', 'TGA']:
                    stops.append(codon)
        if stops:
            f_out.write(f'>{current_gene} {" ".join(sorted(stops))}\n')
            f_out.write(seq + '\n')
print("Done! Output written to stop_genes.fa")