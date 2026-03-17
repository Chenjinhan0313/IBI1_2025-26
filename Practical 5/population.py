countries=['UK','China','Italy','Brazil','USA']
population_2020={'UK':66.7,'China':1426,'Italy':59.4,'Brazil':208.6,'USA':331.6}
population_2024={'UK':69.2,'China':1410,'Italy':58.9,'Brazil':212.0,'USA':340.1}
percent_change=[]
for i in population_2020:
    pc=(population_2024[i]-population_2020[i])/population_2020[i]*100
    percent_change.append(pc)
country_change_pairs=list(zip(countries,percent_change))
print(country_change_pairs)
sorted_pairs=sorted(country_change_pairs,key=lambda x:x[1],reverse=True)
print('The population changes in descending order is:')
for country,change in sorted_pairs:
    print(f'{country}:{change}')
largest_increased=sorted_pairs[0][0]
largest_decreased=sorted_pairs[-1][0]
print('The country with largest increase:'+largest_increased)
print('The country with largest decrease:'+largest_decreased)
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.bar(countries,percent_change,color='lightblue')
plt.title('Population Percentage Change(2020-2024)')
plt.xlabel('Country')
plt.ylabel('Change(%)')
plt.grid(axis='y',alpha=0.3)
plt.tight_layout()
plt.show()