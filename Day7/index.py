# Exercises - Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Twitter', 'Instagram', 'Snapchat'])

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
it_companies.discard('Twitter')

# 5. What is the difference between remove and discard
# remove() will raise an error if the element is not present in the set
# discard() will not raise an error if the element is not present in the set

# Exercises: Level 2
# 1. Join A and B
A.union(B)

# 2. Find A intersection B
A.intersection(B)

# 3. Is A subset of B
A.issubset(B)

# 4. Are A and B disjoint sets
A.isdisjoint(B)

# 5. Join A with B and B with A
A.union(B)
B.union(A)

# 6. What is the symmetric difference between A and B
A.symmetric_difference(B)

# 7. Delete the sets A and B
del A
del B

# Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(len(age_st) > len(age))

# 2. Explain the difference between the following data types: string, list, tuple and set.
# String is a sequence of characters, list is a sequence of items, tuple is a sequence of items that cannot be changed, set is a collection of unique items.

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(len(unique_words))