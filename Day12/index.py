# Exercises: Day 12

# Exercises: Level 1
# 1. Writ a function which generates a six digit/character random_user_id.
import random
import string

# 1. Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for i in range(6))

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    characters = string.ascii_uppercase + string.digits
    num_of_char = int(input("Enter the number of characters: "))
    num_of_id = int(input("Enter the number of IDs: "))
    for i in range(num_of_id):
        print(''.join(random.choice(characters) for i in range(num_of_char)))

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Exercises: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(num):
    hexa_colors = []
    for i in range(num):
        hexa_colors.append('#' + ''.join(random.choice(string.hexdigits) for i in range(6)))
    return hexa_colors

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    rgb_colors = []
    for i in range(num):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, num):
    if color_type == 'hexa':
        return list_of_hexa_colors(num)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type"

# Exercises: Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_numbers():
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:7]
    