import numpy as np
import matplotlib.pyplot as plt
#1.create a 100*100 grid where all individuals are susceptible
population=np.zeros((100,100))
#2.randomly choose one position in the grid and set it to infected
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#3.define infection probability (beta) and recovery probability(gamma)
beta=0.3
gamma=0.05
for i in range (100):
    #4.a.create a copy of the current population grid
    new_population=population.copy()
    #4.b.find all infected individuals
    infected_rows,infected_cols=np.where(population==1)
    for m, n in zip(infected_rows,infected_cols):
        #4.c.i.for each infected individual,check its 8 neighbouring cells
        for d1 in [-1,0,1]:
            for d2 in [-1,0,1]:
                if d1==0 and d2==0:
                    continue
                nm,nn=m+d1,n+d2
                if 0 <= nm < 100 and 0 <= nn < 100:
                    #4.c.ii.if a neighbour is susceptible,infect it with probability beta
                    if population[nm,nn]==0:
                        if np.random.random()<beta:
                            new_population[nm,nn]=1
        #4.c.iii.the infected individual recovers with probability gamma
        if np.random.random()<gamma:
            new_population[m,n]=2
    #4.d.update the population grid using the modified copy
    population=new_population
    #5.as selected time steps,plot the grid to visualize disease spread
    if i in [0,10,30,50,99]:
        plt.figure(figsize=(6,4),dpi=150)
        plt.title(f'Time {i}')
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.show()