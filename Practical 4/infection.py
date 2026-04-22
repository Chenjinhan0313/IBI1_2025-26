# Pseudocode:
# 1. Initialize variables:
#    total_students = total number of students in the class
#    infected = initial number of infected students
#    growth_rate = infection rate per day (as a decimal)
#    day = counter for number of days elapsed
# 2. Display initial condition
# 3. WHILE infected students < total students:
#    a. Increment day by 1
#    b. Calculate new infections = infected × growth_rate
#    c. Update infected = infected + new_infections
#    d. Display current day and infected count
#    e. IF day exceeds 100 THEN break to prevent infinite loop
# 4. Display final results: total days taken and total infected students
# initialize variables
total_students = 91  # the total population of IBI1 class 
infected = 5         # initial number of infected students 
growth_rate = 0.4    # 40% infection rate per day
day = 0              # days counter

print("Initiating infection silulation...")
print(f"Initial condition：Day 0，infected students:{infected}")

# simulation loop:continue until all students are infected
while infected < total_students:
    day = day + 1  # days increase 1
    # calculate the newly infected students
    new_infections = int(infected * growth_rate) # ensure new_infections is integer
    # update the total infections
    infected = infected + new_infections
    # ensure infected does not exceed total students
    if infected > total_students:
      infected = total_students
    print(f"day：infected population: {infected}")
    #avoid infinate loops
    if day > 100:
        print("warm：imitiations larger than 100 days，perhaps cannot infect all the students")
        break
# diaplay final results
print(f"\n Simulation completed！")
print(f"Total days taken: {day} days")
print(f"Total infected students: {infected} out of {total_students}")