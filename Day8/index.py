# Exercises - Day 8

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Buddy', 'color': 'brown', 'breed': 'Golden Retriever', 'legs': 4, 'age': 3}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'John', 'last_name': 'Doe', 'gender': 'Male', 'age': 25, 'marital_status': 'Single', 'skills': ['Python', 'JavaScript', 'HTML', 'CSS'], 'country': 'USA', 'city': 'New York', 'address': '123 Main St'}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('C++')

# 7. Get the dictionary keys as a list
print(list(student.keys()))

# 8. Get the dictionary values as a list
print(list(student.values()))

# 9. Change the dictionary to a list of tuples using items() method
print(list(student.items()))

# 10. delete one of the items in the dictionary
del student['marital_status']

# 11. Delete one of the dictionaries
del dog