import numpy as np
import matplotlib .pyplot as plt
N=10000
beta=0.3
gamma=0.05
I=[[] for _ in range(11)]
vaccination_rate=[0,10,20,30,40,50,60,70,80,90,100]
for i in vaccination_rate:
    if i ==100:
        susceptible=0
        infected=0
        recovered=N
        I[10]=[0 for _ in range(1001)]
    else:
        vaccinated=int(N*i/100)
        susceptible=N-vaccinated-1
        infected=1
        recovered=vaccinated
        current_I=[infected]
        for j in range(1000):
            conditions_infected=np.random.choice(range(2),susceptible,p=[1-beta*infected/N,beta*infected/N])
            conditions_recovered=np.random.choice(range(2),infected,p=[1-gamma,gamma])
            susceptible-=sum(conditions_infected)
            recovered+=sum(conditions_recovered)
            infected-=sum(conditions_recovered)
            infected+=sum(conditions_infected)
            current_I.append(infected)
        I[int(i/10)]=current_I
from matplotlib import cm
plt.figure(figsize=(6,4))
for m in range(11):
    plt.plot(I[m],label=f'{vaccination_rate[m]}%',color=cm.viridis(m*25))
plt.xlabel('Time')
plt.ylabel('Number of infected')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.grid(True)
plt.show()