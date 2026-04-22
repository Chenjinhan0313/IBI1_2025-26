import pandas as pd
import matplotlib.pyplot as plt
def ward_occupy(admissions,discharges):
    days=[1,2,3,4,5,6,7]
    ward_patients=0
    ward_occupy=[]
    #calculate the number of patients each day and store the data in ward_occupy
    for i, j in zip(admissions,discharges):
        ward_patients+=i
        ward_patients-=j
        ward_occupy.append(ward_patients)
    print('The nunber of patients on the ward for each day:')
    print(ward_occupy)
    #generate a plot showing the ward occupy each day
    plt.figure(figsize=(10,5))
    plt.title('Ward Occupy Each Day',fontsize=20)
    plt.xlabel('Day',fontsize=14)
    plt.ylabel('Number of Patients',fontsize=14)
    plt.plot(days,ward_occupy,color='darkblue',linewidth=2,linestyle='-',marker='o')
    plt.grid(True,alpha=0.3)
    plt.xticks(days)
    return ward_occupy,plt.gcf()
#test the function 
admissions=[3,6,9,7,5,4,2]
discharges=[1,1,1,1,1,1,1]
ward_occupy(admissions,discharges)
plt.show()

    


    
    