import re
stop_codons = ['TAA', 'TAG', 'TGA']
genes={}
def wrap_sequence(seq,width=60):
     return '\n'.join([seq[i:i+width] for i in range (0, len(seq),width)])
with open('Practical 7/yeast.fa', 'r') as f_in, open('Practical 7/stop_genes.fa', 'w') as f_out:
    name = None
    seq = []
    for line in f_in:
        line = line.rstrip() #remove newline character
        if not line:
             continue
        #check if this is a header line (start with '>')
        if re.search(r'^>',line):
            if name and seq:
                genes[name]=''.join(seq)
            header=line[1:]
            name=line[1:].split()[0]
            if 'gene:' in header:
                m=re.search(r'gene:(\S+)',header)
                if m:
                     name=m.group(1)
            seq=[]
        else:
            filtered=re.sub(r'[^ATCGatcg]','',line).upper()
            if filtered:
                seq.append(filtered)
    
    if name and seq:
        genes[name]=''.join(seq)

#find genes with in-frame stop codons
    result = {}

    for gene_name, seq in genes.items():
        #find all ATG positions
        atgs = []
        for i in range(len(seq) - 2):
            if seq[i:i+3] == 'ATG':
                atgs.append(i)
    
        if not atgs:
            continue
    
        #for each stop codon, find all in-frame occurrences and calculate ORF length
        best_stop = None
        best_length = 0
    
        for stop in stop_codons:
            #find all positions of this stop codon
            for i in range(len(seq) - 2):
                if seq[i:i+3] == stop:
                    #check if in-frame with any ATG
                    for atg in atgs:
                        if i > atg and (i - atg) % 3 == 0:
                            orf_length = i - atg + 3
                            if orf_length > best_length:
                                best_length = orf_length
                                best_stop = stop
                            break
    
        #save gene with only the best stop codon
        if best_stop:
            name_new = f"{gene_name}_{best_stop}"
            result[name_new] = seq

    print(f"Genes with in-frame stop codons: {len(result)}")

    #write output
    for name, seq in result.items():
        f_out.write(f">{name}\n")
        f_out.write(wrap_sequence(seq) + "\n")
                
    print("Done! Output shwon in stop_genes.fa")
