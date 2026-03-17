heart_rates=[72,60,126,85,90,59,76,131,88,121,64]
mean_heart_rates=sum(heart_rates)/len(heart_rates)
print("There are "+str(len(heart_rates))+" patients in the dataset")
print("The mean heart rates is:"+str(mean_heart_rates)+"bpm")
low=0
normal=0
high=0
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
if low > normal and low > high:
    max="low"
elif normal > high:
    max="normal"
else:
    max="high"
print("The largest category is:"+max)
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels=['Low(<60 bpm)','Normal(60-120 bpm)','High(>120 bpm)']
sizes=[low,normal,high]
colors=['lightblue','lightpink','yellow']
explode=(0.01,0.01,0.01)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
