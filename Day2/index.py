# Exercise - Day2

# Exercise Level1
# Day 2: 30 Days of python programming
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = 'Asabeneh Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
year = 2025
is_married = True
is_true = True
is_light_on = False
first_name, last_name, country, city, age, year, is_married, is_true, is_light_on = 'Asabeneh', 'Yetayeh', 'Finland', 'Helsinki', 250, 2025, True, True, False

# Exercise Level2
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
print('Is last name length greater than first name length? ', len(last_name) > len(first_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = int(input('Enter the radus of the circle: '))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print('Area of the circle is: ', area_of_circle)
print('Circumference of the circle is: ', circum_of_circle)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')
help('keywords')