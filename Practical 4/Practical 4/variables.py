# Population Growth Analysis
# PSEUDOCODE:
# 1. Assign population values for years 2004, 2014, 2024
# 2. Calculate population change for 2004-2014 (d = b - a)
# 3. Calculate population change for 2014-2024 (e = c - b)
# 4. Display both population changes
# 5. Compare d and e:
#    - IF d > e THEN growth is decelerating
#    - ELSE growth is accelerating
# 6. Display the result with a comment explaining the trend
# 7. Demonstrate Boolean logic:
#    - Set X = True, Y = False
#    - Calculate W = X OR Y
#    - Display result

# Population data for three time points (in millions)
a = 5.08  # Population in 2004
b = 5.33  # Population in 2014
c = 5.55  # Population in 2024

# Calculate population changes between periods
d = b - a  # Change from 2004 to 2014
e = c - b  # Change from 2014 to 2024

# Output the calculated changes
print(f"2004-2014 population change: {d} million")
print(f"2014-2024 population change: {e} million")

# Compare the two periods to determine growth trend
# If the first period's increase is larger than the second,
# the population growth is slowing down (decelerating)
if d > e:
    print("The increase of population is decelerating")
else:
    # If the second period's increase is larger or equal,
    # the population growth is speeding up (accelerating)
    print("The increase of population is accelerating")

# Boolean logic demonstration: OR operator
X = True
Y = False
W = X or Y  # OR operation: True if at least one is True
print(f"The result of X or Y is: {W}")

# Optional: Truth table reference for OR operator
# X=True, Y=True  -> W=True
# X=True, Y=False -> W=True
# X=False, Y=True -> W=True
# X=False, Y=False -> W=False