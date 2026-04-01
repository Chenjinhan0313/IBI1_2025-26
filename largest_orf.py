seq='AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG' 
import re
ORF=re.findall(r'AUG.*?UAA|AUG.*?UAG|AUG.*?UGA',seq)
print(ORF)
max=0
for i in ORF:
    if len(i) > max:
        max=len(i)
        largest_ORF=i
print("The largest ORF is:")
print(largest_ORF)
print("The length of it is:")
print(max)
