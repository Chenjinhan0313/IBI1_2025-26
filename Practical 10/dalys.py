import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('C:/Users/lenovo/Downloads')
dalys_data =pd.read_csv('dalys-rate-from-all-causes.csv')
dalys_data.head(5)
dalys_data.info()
# 1. The data points are of types: str, int64, and float64.
# 2. The columns are: Entity, Code, Year, DALYs.
# 3. There are 6840 rows in total.
print(dalys_data.describe())
#output:
#          Year          DALYs
#count  6840.000000    6840.000000
#mean   2004.500000   42372.219173
#std       8.656074   22596.140799
#min    1990.000000   15045.110000
#25%    1997.000000   26973.065000
#50%    2004.500000   35035.490000
#75%    2012.000000   52732.695000
#max    2019.000000  693367.490000
print(dalys_data.iloc[0,3])#access values by row and column numbers
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])
#how I show the third and fourth colums (the year and the DALYs) for the first 10 rows?
print(dalys_data.iloc[0:10,2:4])
#year 1998 reported the maximum DALYs across the first 10 years
print(dalys_data.iloc[0:3,[0,1,3]])#only show the first,second and fourth columns of the first three rows
#another way
my_columns=[True,True,False,True]
print(dalys_data.iloc[0:3,my_columns])
print('Comment:Year 1998 recorded the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan')
#what if it is shorter?
my_columns=[True,True,False]
print(dalys_data.iloc[0:3],my_columns)
#result:
#        Entity Code  Year     DALYs
#0  Afghanistan  AFG  1990  86375.17
#1  Afghanistan  AFG  1991  83381.07
#2  Afghanistan  AFG  1992  79890.55 [True, True, False]
#what if it is longer?
my_columns=[True,True,False,True,False]
print(dalys_data.iloc[0:3],my_columns)
#result:
#        Entity Code  Year     DALYs
#0  Afghanistan  AFG  1990  86375.17
#1  Afghanistan  AFG  1991  83381.07
#2  Afghanistan  AFG  1992  79890.55 [True, True, False, True, False]
print(dalys_data.loc[2:4,'Year'])#access adta by row nunmers and column names (that is because row don't have names)
#1. How do you read just the “Year” column, but all the rows from dalys_data?
dalys_data.loc[:,'Year']
#2. How can you create a Boolean that is True when the “Entity” is “Zimbabwe”, but false otherwise? (Recall from lecture 4.2 how to check whether something is equal to something else)
boolean=dalys_data['Entity'] == 'Zimbabwe'
#3. How do you use that Boolean to find exactly the rows you need in your dataframe?
print(dalys_data.loc[boolean,:])
print('Comment:the first year these data were recorded:1990' \
'the last year these data were recorded:2019')
boolean2=dalys_data['Year'] == 2019
dalys_data_proccesed=dalys_data.loc[boolean2,:]
print(dalys_data_proccesed.describe())
boolean3=dalys_data_proccesed['DALYs'] == 90771.64
print(f'{dalys_data_proccesed.loc[boolean3,:].loc[:,'Entity'].iloc[0]} recorded the largest DALYs values in the most recent year')
boolean4=dalys_data_proccesed['DALYs'] == 15045.11
print(f'{dalys_data_proccesed.loc[boolean4,:].loc[:,'Entity'].iloc[0]} recorded the smallest DALYs value in the most recent year ')
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
singapore_Year=dalys_data.loc[dalys_data['Entity'] == 'Singapore','Year']
singapore_DALYs=dalys_data.loc[dalys_data['Entity'] == 'Singapore','DALYs']
plt.plot(singapore_Year, singapore_DALYs, 'bo')
# b+---blue '+'   r+---red '+'   bo---blue dot
plt.xticks(singapore_Year,rotation=-90)
#rotation represents the rotation of the mark of singapore_Year
plt.show()
#question answering code
china_data=dalys_data.loc[dalys_data.Entity == 'China',['Year','DALYs']]
uk_data=dalys_data.loc[dalys_data.Entity == 'United Kingdom',['Year','DALYs']]
plt.plot(china_data['Year'],china_data['DALYs'],label='China',color='red')
plt.plot(uk_data['Year'],uk_data['DALYs'],label='UK',color='blue')
plt.title('The relationship between the DALYs in China and the UK changed over time')
plt.show()

