# initialize variables
total_students = 91  # the total population of IBI1 
infected = 5          
growth_rate = 0.4     # 40% increasing rate
day = 0               # days calculator

print("begin imitiating infection...")
print(f"initial condition：zero day，infected population:{infected}")

# when the number of infected students is smaller than the total students
while infected < total_students:
    day = day + 1  # days increase 1
    
    # calculate the newly increases infections
    new_infections = infected * growth_rate
    
    # update the total infections
    infected = infected + new_infections
    
    print(f"day：infected population: {infected}")
    
    #avoid infinate loops
    if day > 100:
        print("warm：imitiations larger than 100 days，perhaps cannot infect all the students")
        break

print(f"\n imtiations finish！")
print(f"use totally {day} days,infect totally {infected} students")