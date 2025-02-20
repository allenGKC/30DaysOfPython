# Exercises: Day 5
# Exercises: Level 1
# 1. Declare an empty list
list = []

# 2. Declare a list with more than 5 items
list = [1, 2, 3, 4, 5, 6]

# 3. Find the length of your list
print(len(list))

# 4. Get the first item, the middle item and the last item of the list
first_item = list[0]
middle_item = list[len(list) // 2]
last_item = list[-1]
print(first_item, middle_item, last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John', 25, 5.11, 'single', '123 Main St']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Twitter'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Linkedin')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Yahoo')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()

# 14. Join the it_companies with a string '#; '
print('#; '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('Facebook' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies) // 2])

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)

# 23. Remove the last IT company from the list
it_companies.pop()

# 24. Remove all IT companies
it_companies.clear()

# 25. Destroy the list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

# Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# 2. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(min_age, max_age)
# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# 3. Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages) // 2]
print(median_age)

# 4. Find the average age (the sum of all items divided by the number of items)
average_age = sum(ages) / len(ages)

# 5. Find the range (max minus min)
range_age = max_age - min_age

# 6. Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age - average_age), abs(max_age - average_age))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

# 1. Find the middle country(ies) in the countries list
middle_country = countries[len(countries) // 2]
print(middle_country)

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
half_countries = len(countries) // 2
first_half = countries[:half_countries]
second_half = countries[half_countries:]
print(first_half, second_half)

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(china, russia, usa)
