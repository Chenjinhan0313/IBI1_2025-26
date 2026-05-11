import re
import matplotlib.pyplot as plt
#get user input
stop_input = input("Enter a stop codon (TAA, TAG, or TGA): ").rstrip().upper()
while stop_input not in ['TAA', 'TAG', 'TGA']:
    stop_input = input("Invalid input. Please enter TAA, TAG, or TGA: ").rstrip().upper()
#read stop_genes.fa
genes = []
with open('Practical 7/stop_genes.fa', 'r') as f:
    current_gene = None
    current_seq = []
    for line in f:
        line = line.rstrip()
        if re.search(r'^>',line):
            if current_gene and current_seq:
                genes.append((current_gene, ''.join(current_seq)))
            pos=line.find('>')
            end=line.find(' ',pos)
            current_gene=line[pos+1:end]
            current_seq = []
        else:
            if line:
                current_seq.append(line)
    if current_gene and current_seq:
        genes.append((current_gene, ''.join(current_seq)))
#count codons upstream of the longest ORF ending with the specified stop codon
codon_count = {}
for current_gene,current_seq in genes:
    #find first start codon
    start = current_seq.find('ATG')
    if start == -1:
        continue
    #find all stop positions
    stop_positions = []
    for i in range(start, len(current_seq)-2, 3):
        codon = current_seq[i:i+3]
        if codon in ['TAA', 'TAG', 'TGA']:
            stop_positions.append(i)
    #find the stop codon that gives the longest ORF
    best_stop=None
    best_orf_length=0
    for m in stop_positions:
        if current_seq[m:m+3] == stop_input:
            orf_length=m-start+3
            if orf_length>best_orf_length:
                best_orf_length=orf_length
                best_stop=m
    #count codons upstream of the chosen stop codon
    if best_stop != None:
        for i in range(start, best_stop, 3):
            codon = current_seq[i:i+3]
            if codon in codon_count:
                codon_count[codon]+=1
            else:
                codon_count[codon]=1
#display results
print(f"\nCodon usage upstream of {stop_input}:")
for codon in codon_count:
    count=codon_count[codon]
    print(f"{codon}: {count}")
#generate pie chart
if codon_count:
    labels = list(codon_count.keys())
    sizes = list(codon_count.values())
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Codon usage upstream of {stop_input}')
    plt.savefig(f'codon_usage_{stop_input}.png')
    plt.close()
    print(f"\nPie chart saved as codon_usage_{stop_input}.png")
else:
    print(f"\nNo genes found with {stop_input} stop codon.")
