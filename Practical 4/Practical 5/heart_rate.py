#restore the statistics in a list
heart_rates=[72,60,126,85,90,59,76,131,88,121,64]
#calculate the mean of those heart rates
mean_heart_rates=sum(heart_rates)/len(heart_rates)
print("There are "+str(len(heart_rates))+" patients in the dataset")
print("The mean heart rates is:"+str(mean_heart_rates)+"bpm")
#initialize the number of patients in each category
low=0
normal=0
high=0
#calculate the total number of patients of each category
for i in heart_rates:
    if i < 60:
        low+=1
    elif i <=120:
        normal+=1
    else:
        high+=1
print(f"Heart rates categories:")
print(f"Low:{low} patients")
print(f"Normal:{normal} patients")
print(f"High:{high} patients")
#compare the population of each category and output the category with the largest number of patients
if low > normal and low > high:
    max="low"
elif normal > high:
    max="normal"
else:
    max="high"
print("The largest category is:"+max)
import matplotlib.pyplot as plt
#create figure with width about 10 inch and height about 6 inch
plt.figure(figsize=(8,8))
#give each part a label indicating its category
labels=['Low(<60 bpm)','Normal(60-120 bpm)','High(>120 bpm)']
sizes=[low,normal,high]
#give each part a unique color
colors=['lightblue','lightpink','yellow']
explode=(0.01,0.01,0.01)
plt.title("Distribution of Patients in Each Category")
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
