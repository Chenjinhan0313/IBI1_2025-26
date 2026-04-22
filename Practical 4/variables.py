# Pseudocode:
# 1. Define population data for three time points (unit: million)
#    a = population in 2004
#    b = population in 2014  
#    c = population in 2024
# 2. Calculate population changes for two periods
#    d = population change from 2004 to 2014 = b - a
#    e = population change from 2014 to 2024 = c - b
# 3. Output population changes for both periods
# 4. Compare d and e to determine population growth trend
#    If d > e then population growth is decelerating
#    ELSE population growth is accelerating
# 5. Define boolean variables X = True, Y = False
# 6. Calculate logical OR operation W = X OR Y
# 7. Output the result of W

# Define population data for three time point
a = 5.08   # Population in 2004
b = 5.33   # Population in 2014
c = 5.55   # Population in 2024
# Calculate population changes for two periods
d=b-a # Variable d: population change from 2004 to 2014
e=c-b # Variable e: population change from 2014 to 2024

# Output population change data
print(f"2004-2014 population change：{d} million")
print(f"2014-2024 population change：{e} million")

# Determine population growth trend and add explanatory comment
# Comment: Compare population growth between two periods to determine trend
# If first period growth is greater than second period, growth is decelerating
# Otherwise, growth is accelerating
if d > e:
    print("Population growth is decelerating")
    # Comment: d > e, growth rate is decreasing, indicating deceleration
else:
    print("Population growth is accelerating")
    # Comment: d ≤ e, growth rate is increasing or constant, indicating acceleration

# Logical operation test
X = True
Y = False
W = X or Y  # Calculate logical OR operation of X and Y
print(f"The result of X OR Y is: {W}")

# Truth table verification
print(" Truth Table for OR Operation ")
print("X\tY\tW = X OR Y")
print("-" * 20)

# Test all possible combinations
combinations = [(True, True), (True, False), (False, True), (False, False)]

for X, Y in combinations:
    W = X or Y
    print(f"{X}\t{Y}\t{W}")

# Verification results:
# True OR True = True
# True OR False = True  
# False OR True = True
# False OR False = False