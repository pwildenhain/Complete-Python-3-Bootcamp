# learning about built in operators in python that
# will be useful for accomplishing different programming tasks

# the range keyword allows us to create lists of numbers
# instead of 
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist
# We can do
myrange = range(11)
myrange
# A range is an iterable that can used in for loops
for num in mylist:
    print(num)
# Same result
for num in myrange:
    print(num)
# Other arguments, are the start and step
# The start argument is inclusive, while the stop argument is exclusive
# Just like slicing with strings and lists/tuples/dicts
myrange = range(5, 10)
for num in myrange:
    print(num)
# Also just like slicing, you can step over integers, 
# and count backward
# Odd numbers 1 to 10
myrange = range(1, 11, 2)
for num in myrange:
    print(num)
# Count backward from 5. Now start will be the larger number
myrange = range(5, -1, -1)
for num in myrange:
    print(num)
# Remember a range is a generator, so it just saves the information
# with the data you give it, and only evaluates it when it needs to
# like being used in a loop
myrange = range(0, 10)
# Prints range(0, 10)
myrange
# If we want to see it, we can cast it to a list
list(myrange)

# enumerate is useful when we want to keep track on which number
# the current iteration is on.
name = 'Wildenhain'
for item in enumerate(name):
    print(item)
# Ta-da! Python counts the iterations for us, and give us tuples
# which means we can unpack them
for index, letter in enumerate(name):
    print(f'Letter number {index + 1} is {letter}')
# Next is the zip function, which will combine 
# objects into tuples, which can then be unpacked
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']
# By itself, it doesn't return anything, but it lets me 
# know where it's saved in my memory
zip_obj = zip(numbers, letters, symbols)
zip_obj
for item in zip_obj:
    print(item)
# You actually can't unpack zip_obj. Since it
# is only doing the zipping during the loop, or other iteration
# similar to using enumerate in the for loop
for number, letter, symbol in zip(numbers, letters, symbols):
    print(f'{number} : {letter} : {symbol}')
# Keep in mind, zip will only zip together even lenthged objects
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b']
# this is only going to zip up to two
for item in zip(numbers, letters):
    print(item)
# We can also just cast to a list of the nested tuples
list(zip(letters, numbers))
# again, you can't use the zip object to do this
list(zip_obj)

# the in operator to check for existence
'x' in 'xlksdjlsk'
# in a list
'x' in ['x', 'y', 'z']
# in a dict
'x' in {'x': 1}

# min and max to get the min/max of a list
numbers = [1, 2, 3, 4]
min(numbers)
max(numbers)


# using the built in random library to randomize stuff
from random import shuffle

numbers
# it doesn't return anything, it just effects the object itself
# operating in place
shuffle(numbers)
# return it
numbers

# getting a random integer
from random import randint
randint(0, 10)

# Lastly, accepting user input
answer = input('Favorite color? ')
# Prompts for an answer
answer
# Rememeber, it only returns strings
















