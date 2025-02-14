# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


# Exercise: Level 2
# Q2.
print(3 + 4) # addition(+)
print(3 - 4) # subtraction(-)
print(3 * 4) # multiplication(*)
print(3 % 4) # modulus(%)
print(3 / 4) # division(/)
print(3 ** 4) # exponential(**)
print(3 // 4) # Floor division operator(//)

# Q3
print('Allen') # Your name
print('Gong') # Your family name
print('China') # Your country
print('I am enjoying 30 days of python') # A message

# Q4
print(type(10)) # Int
print(type(9.8)) # Float
print(type(3.14)) # Float
print(type(4 - 4j)) # Complex number
print(type(['Asabeneh', 'Python', 'Finland'])) # List
print(type('Allen')) # String
print(type('Gong')) # String
print(type('China')) # String

# Exercise: Level 3
"""
Find an Euclidian distance between (2, 3) and (10, 8)
"""
# Q1
import math

point1 = (2, 3)
point2 = (10, 8)

distance = math.dist(point1, point2)

print('The distance between the two points is ', distance)


