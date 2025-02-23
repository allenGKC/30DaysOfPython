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




