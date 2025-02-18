# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2


# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))


# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3


# Comparing something gives either a True or False
 
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# Exercises - Day 3
base = input('Enter the base of the triangle: ')
height = input('Enter the height of the triangle: ')
area = 0.5 * int(base) * int(height)
print('The area of the triangle is', area)

side_a = input('Enter the length of side a: ')
side_b = input('Enter the length of side b: ')
side_c = input('Enter the length of side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print('The perimeter of the triangle is', perimeter)

width = input('Enter the width of the rectangle: ')
length = input('Enter the length of the rectangle: ')
area = int(width) * int(length)
perimeter = 2 * (int(width) + int(length))
print('The area of the rectangle is', area)
print('The perimeter of the rectangle is', perimeter)

radius = input('Enter the radius of the circle: ')
pi = 3.14
area = pi * (int(radius) ** 2)
circumference = 2 * pi * int(radius)
print('The area of the circle is', area)
print('The circumference of the circle is', circumference)


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon')) # False

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon') # True

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon') # True

# Find the length of the text python and convert the value to float and convert it to string
print(float(len('python'))) # 6.0
print(str(len('python'))) # '6'

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Enter a number: '))
if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7)) # True

# Check if type of '10' is equal to type of 10
print(type('10') == type(10)) # False

# Check if int('9.8') is equal to 10
print(int('9.8') == 10) # False

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter the number of hours: '))
rate = int(input('Enter the rate per hour: '))
pay = hours * rate
print('Your pay is', pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter the number of years: '))
seconds = years * 365 * 24 * 60 * 60
print('You have lived for', seconds, 'seconds')

# Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

for n in range(1, 6):
    print(f"{n} 1 {n} {n**2} {n**3}")




