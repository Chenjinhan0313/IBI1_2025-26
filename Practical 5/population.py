#store all the countries in a list for further use
countries=['UK','China','Italy','Brazil','USA']
#store each country's population in two dictionaries,showing the population of 2020 and 2024 respectively
population_2020={'UK':66.7,'China':1426,'Italy':59.4,'Brazil':208.6,'USA':331.6}
population_2024={'UK':69.2,'China':1410,'Italy':58.9,'Brazil':212.0,'USA':340.1}
#set an empty list named percent_change for further store
percent_change=[]
#use the equation to calculate the percent change of each country and store them in percent_change
for i in population_2020:
    pc=(population_2024[i]-population_2020[i])/population_2020[i]*100
    percent_change.append(pc)
#combine two lists(countries and percent_change) together so I can sort the percent change value with the indexes changing together.
country_change_pairs=list(zip(countries,percent_change))
print("The population change of each country is as follows:")
print(country_change_pairs)
#sort the combined list in a descending order
sorted_pairs=sorted(country_change_pairs,key=lambda x:x[1],reverse=True)
print('The population changes in descending order is:')
for country,change in sorted_pairs:
    print(f'{country}:{change}')
#use indexing to obtain the country names with largest increased/decreased 
largest_increased=sorted_pairs[0][0]
largest_decreased=sorted_pairs[-1][0]
print('The country with largest increase:'+largest_increased)
print('The country with largest decrease:'+largest_decreased)
#create a bar chart to show the population change of each country
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.bar(countries,percent_change,color='lightblue')
plt.title('Population Percentage Change(2020-2024)')
plt.xlabel('Country')
plt.ylabel('Change(%)')
plt.grid(axis='y',alpha=0.3)
plt.tight_layout()
plt.show()