# Exercises: Day 13

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negtive_and_zero_numbers = [n for n in numbers if n <= 0]
print(negtive_and_zero_numbers)

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
fflattened_list = [ number for row in list_of_lists for n in row for number in n]
print('f_list', fflattened_list)


# 3. Using list comprehension create the following list of tuples:
'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''
list_of_tuples = [(i, 1, i**j, i**j, i**j, i**j, i**j) for i in range(11) for j in range(7)]
# print('list_of_tuples', list_of_tuples)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_flattened_list = [country for row in countries for country in row]
print('new_flattened_list', new_flattened_list)

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list_of_dicts = [{'country': country[0], 'city': country[1]} for row in countries for country in row]
print('new_list_of_dicts', new_list_of_dicts)

# 6.Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_string = [f'{name[0]} {name[1]}' for row in names for name in row]
print('new_string', new_string)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - (m * x)

# Example usage
x1, y1 = 0, 1  # First point
x2, y2 = 2, 5  # Second point

m = slope(x1, x2, y1, y2)
b = y_intercept(x1, y1, m)

print('Slope (m):', m)
print('Y-intercept (b):', b)
print('Linear equation: y =', m, 'x +', b)
