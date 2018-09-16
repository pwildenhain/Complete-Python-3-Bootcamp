# Tuples are very similar to lists, except they are immutable, and use parentheses
# Meaning, once and element is inside a tuple it cannot be reassigned
# Like, you would have to create a new tuple object to achieve that
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
type(my_tuple)
type(my_list)
# Can stil check the length
len(my_tuple)
# Can hold multiple object types
my_tuple = ('one', 2)
my_tuple
# Can still use slicing and indexing
my_tuple[0]
my_tuple[-1]
# Useful built in methods
# Return the position of an item in the tuple
my_tuple.index(2)
# How does this work for repeat items?
test_tuple = ('a', 'b', 'b', 'c')
test_tuple.index('b')
# Ok, it just returns the first
# Can I use a for loop to return all the instances
for item in test_tuple:
    if item == 'b':
        print(test_tuple.index(item))
# This just returns 
# >>> 1
# >>> 1
# Because it's still grabbing the first appearance
# I'm not going to get this to work with the index method
# This will work but it's a little ugly
for i in range(0,len(test_tuple)):
    if test_tuple[i] == 'b':
        print(i) 
# Can you index with lists?
test_list = ['a', 'b', 'b', 'c']
# Hmm, it doesn't seem like it
test_list.index['c'] # <- Returns error
# Count how often an item appears in a tuple
my_tuple.count('one')
# Again, can we do this with lists?
test_list.count('b')
# Ok cool, we can do that with lists
# showing off immutability
my_list
# No prob with reassigning values
my_list[0] = 0
my_list
# But tuples don't allow that
my_tuple
my_tuple[0] = 0 # <- Throws an error
# So if they have fewer methods, AND the are immutable, why use them?
# Well if you're doing advanced programming, you might need to pass around
# objects/values that you want to make sure don't accidentally get changed.
# Tuples will do that job well for you, because they'll throw an error if you
# try to change them. This is known as data integrity
