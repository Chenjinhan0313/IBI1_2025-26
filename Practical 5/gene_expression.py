#create and print a dictionary containing the genes and their expression values.
gene_expression={"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
#add the expression of gene named "MYC"
gene_expression["MYC"]=11.6
print("Gene Expression:")
print(gene_expression)
print()
#create a bar chart to show the gene_expreesion 
import numpy as np
import matplotlib.pyplot as plt
#create figure with width about 10 inch and height about 6 inch
plt.figure(figsize=(10,6))
#draw the figure with x about gene and y about genes'expression
plt.bar(gene_expression.keys(),gene_expression.values(),color='steelblue')
#add title,xlabel and ylabel to the chart
plt.title("Gene Expression Levels",fontsize=16)
plt.xlabel("Genes",fontsize=12)
plt.ylabel("Expression Value",fontsize=12)
plt.grid(axis='y',alpha=0.3)
#adjust the layout automatically
plt.tight_layout()
#save the figure 
plt.savefig("gene_expression_chart.png")
plt.show()
gene_of_interest="TP53"#This can be modified manually
#Check if a gene of interest exists in the dataset and output its expression value or an error message
if gene_of_interest in gene_expression:
    print("The expression value of this gene is:")
    print(gene_expression[gene_of_interest])
else:
    print("This gene is not present in the dataset")
#calculate the average of all gene expression present in the dataset
sum=0
for i in gene_expression:
    sum+=gene_expression[i]
average=sum/len(gene_expression)
print("The average gene	expression level across	all	genes is:")
print(average)