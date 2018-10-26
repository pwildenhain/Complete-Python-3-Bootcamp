# loops are used along with iterable
# iterable == perform an action for every elements, working through it
my_iterable = [1, 2, 3]
for element in my_iterable:
    print(element)
# You can choose whatever variable name is most readable
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_list:
    print(number)
# I techincally don't even need to use any of these items
# in order to iterate with them
for number in my_list:
    print('hi')
# Can use more control flow inside loop
# Tell me about the number
for number in my_list:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
# Keeping a running total of a list
list_sum = 0

for number in my_list:
    list_sum += number
    # Get the running total
    print(list_sum)

# Get total at end
print(list_sum)
# Strings can also be iterated over
my_string = 'Vertical'

for letter in my_string:
    print(letter)
# Again, you don't even need to use the thing in order to iterate
my_string = 'Vertical'

for _ in my_string:
    print('Horizontal')
# Print out tuples in a list
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for tup in my_list:
    print(tup)
# Tuples have a special property in python called 
# "tuple unpacking" and it works like this
# Parentheses are not required
for (first, second) in my_list:
    print(first)
    print(second)
# By duplicating the STRUCTURE of the items in the sequence,
# you can take advantage of this unpacking by using the 
# objects in your loops. I could potentially take advantage of 
# this in my budget, where the sql query returns a list of
# tuples. I could potentially get rid of the pandas dependency

# What happens if the structure isn't the same
my_messed_up_list = [(1, 2), (3, 4, 5), (6, 7)]
# throws a ValueError right away, saying there are too many 
# values to unpack. That's good
for a, b in my_messed_up_list:
    print(a)
# Iterating through a dictionary
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}
# Defaults to only printing keys
for item in my_dict:
    print(item)
# If we want to work with the items we have to change it up
# and this returns tuple pairs
for item in my_dict.items():
    print(item)
# since we get back tuples, we can use the tuple unpacking method described above
for key, value in my_dict.items():
    print(f'Key = {key} Value = {value}')
# We can also choose to only iterate over the values
for value in my_dict.values():
    print(value)
# Keep in mind a dictionary is not ordered
# What if I have different type of values?
my_messy_dict = {'k1': 1, 'k2': [2, 3], 'k3': {'a': 1, 'b': 2}}
# Ok so it's just going to use the raw keys and values
# Still just tuple pairs
for key, value in my_messy_dict.items():
    print(f'Key = {key} Value = {value}')


















