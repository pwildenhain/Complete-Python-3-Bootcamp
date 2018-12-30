# List comprehensions are neat ways to create lists in python
# Basically, rather than looping through an iterable and .append()'ing
# every time, you could do a list comprehension instead. I think I can
# definitely use this in the D&D project

# Make a list that contains every letter in the word
mystring = 'hello'
mylist = []
# With a for loop
for letter in mystring:
    mylist.append(letter)

mylist
# With a list comprehension
# It takes the iterable, and automatically performs the 
# calculations in the creation of the variable
# it assumes the only action you want to perform on the 
# LIST is append(), and you can perform other actions
# on the iterable
mylist = [letter for letter in mystring]
mylist
# Easily creating a list with a range of numbers
mynumlist = [num for num in range(0, 11)]
mynumlist
# Perform operations on the element in the iterable
mysquarelist = [num**2 for num in range(0, 11)]
mysquarelist
# Can even add conditionals to the end of the comprehension
myevenlist = [num for num in range(0, 11) if num % 2 == 0]
myevenlist
# You can do if else, but the order has to be reversed
myweirdlist = [num if num % 2 == 0 else 'ODD' for num in range(0, 11)]
myweirdlist
# You can also doing nesting with list comprehension
# Example of a nested loop
nestedlooplist = []
for num in [1, 2, 3]:
    for multiplier in [1, 10, 100]:
        nestedlooplist.append(num * multiplier)

nestedlooplist
# Example of nested list comprehension
nestedcomplist = [num * multiplier for num in [1, 2, 3] for multiplier in [1, 10, 100]]
nestedcomplist
