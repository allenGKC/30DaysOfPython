# Exercises - Day 9

# Exercises: Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} years to drive.")


# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
    print(f"I am {my_age - your_age} years older than you.")
elif my_age < your_age:
    print(f"You are {your_age - my_age} years older than me.")
else:
    print("We are the same age.")


# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2
'''
1. Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
score = int(input("Enter your score: "))
if score >= 80 and score <= 100:
    print("Grade A")
elif score >= 70 and score <= 89:
    print("Grade B")
elif score >= 60 and score <= 69:
    print("Grade C")
elif score >= 50 and score <= 59:
    print("Grade D")
else:
    print("Grade F")

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month: ")
autumn = ['September','October','November']
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']

if month in autumn:
    print("Autumn")
elif month in winter:
    print("Winter")
elif month in spring:
    print("Spring")
elif month in summer:
    print("Summer")
else:
    print("Invalid month")

# 3. The following list contains some fruits:
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)

# Exercises: Level 3
# 1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

'''
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''
if 'skills' in person:
    print(person['skills'][len(person['skills'])/2])
else:
    print("No skills")

if 'skills' in person:
    if 'Python' in person['skills']:
        print("He has Python",person['skills'])
    else:
        print("He doesn't have Python")
else:
    print("No skills")

if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("He is a front end developer")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a fullstack developer")
    else:
        print("unknown title")
else:
    print("No skills")

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland")
else:
    print("Invalid")



    