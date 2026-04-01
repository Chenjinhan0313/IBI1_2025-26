import re
import matplotlib.pyplot as plt
stop_input = input("Enter a stop codon (TAA, TAG, or TGA): ").rstrip().upper()
while stop_input not in ['TAA', 'TAG', 'TGA']:
    stop_input = input("Invalid input. Please enter TAA, TAG, or TGA: ").rstrip().upper()
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
codon_count = {}
for current_gene,current_seq in genes:
    start = current_seq.find('ATG')
    if start == -1:
        continue
    stop_positions = []
    for i in range(start, len(current_seq)-2, 3):
        codon = current_seq[i:i+3]
        if codon in ['TAA', 'TAG', 'TGA']:
            stop_positions.append(i)
    found = False
    for m in stop_positions:
        if current_seq[m:m+3] == stop_input:
            found = True
            break
    if not found:
        continue
    last_stop = None
    for pos in stop_positions:
        if current_seq[pos:pos+3] == stop_input:
            last_stop = pos
    if last_stop != None:
        for i in range(start, last_stop, 3):
            codon = current_seq[i:i+3]
            if codon in codon_count:
                codon_count[codon]+=1
            else:
                codon_count[codon]=1
print(f"\nCodon usage upstream of {stop_input}:")
for codon in codon_count:
    count=codon_count[codon]
    print(f"{codon}: {count}")
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