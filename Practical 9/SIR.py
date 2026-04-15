import numpy as np
import matplotlib .pyplot as plt
susceptible=9999
infected=1
recovered=0
N=10000
beta=0.3
gamma=0.05
S,I,R=[susceptible],[infected],[recovered]
for i in range(1000):
    conditions_infected=np.random.choice(range(2),susceptible,p=[1-beta*infected/N,beta*infected/N])
    conditions_recovered=np.random.choice(range(2),infected,p=[1-gamma,gamma])
    susceptible-=sum(conditions_infected)
    recovered+=sum(conditions_recovered)
    infected-=sum(conditions_recovered)
    infected+=sum(conditions_infected)
    S.append(susceptible),I.append(infected),R.append(recovered)
plt.figure(figsize=(6,4))
plt.plot(S,label='Susceptible',color='blue')
plt.plot(I,label='Infected',color='red')
plt.plot(R,label='Recovered',color='green')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model')
plt.legend()
plt.grid(True)
plt.show()
