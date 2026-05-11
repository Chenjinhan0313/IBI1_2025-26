# 1. Create a 100x100 grid of zeros (all susceptible)
# 2. Randomly choose one cell to be infected (set to 1)
# 3. Set beta = 0.3, gamma = 0.05
# 4. For each time step (0 to 99):
#    a. Copy the current grid
#    b. Find all infected cells
#    c. For each infected cell:
#       i. For each of its 8 neighbours:
#          - If neighbour is susceptible, infect with probability beta
#       ii. Recover this infected cell with probability gamma
#    d. Update grid with the copy
#    e. At specific times (0,10,30,50,99), plot the gridimport numpy as np
import matplotlib.pyplot as plt
import numpy as np
#1.create a 100*100 grid where all individuals are susceptible
population=np.zeros((100,100))
#2.randomly choose one position in the grid and set it to infected
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#3.define infection probability (beta) and recovery probability(gamma)
beta=0.3
gamma=0.05
snapshots={}
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
        snapshots[i]=population.copy()
# Time 0 in a single picture   
plt.figure(figsize=(6,4),dpi=150)
plt.title(f'Time {i}')
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.savefig(f'disease_spread_time_0.png',bbox_inches='tight',dpi=150)
plt.close()
# Time 10,30,50,99 place in 2*2 picture
fig, axes = plt.subplots(2, 2, figsize=(10, 10), dpi=150)
time_points = [10, 30, 50, 99]
titles = ['Time 10', 'Time 30', 'Time 50', 'Time 99']

for ax, t, title in zip(axes.flat, time_points, titles):
    ax.imshow(snapshots[t], cmap='viridis', interpolation='nearest')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig('disease_spread_time_10_99_combined.png', bbox_inches='tight', dpi=150)
plt.close()
print("Done! Figures have been saved to figure folder!")
        
