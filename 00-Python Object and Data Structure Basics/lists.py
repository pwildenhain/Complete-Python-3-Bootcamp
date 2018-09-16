my_list = ['one', 'two', 'three']
another_list = ['four', 'five']
new_list = my_list + another_list
new_list
# Indexing
new_list[0] = 'ONE'
# Automatically adds to the end of the list
new_list.append('six')
new_list.append('seven')
# Pops out the last element, and returns
new_list.pop()
# Now seven is gone
new_list
# Saved the popped item
popped_item = new_list.pop()
popped_item
# pop() method defaults to the end of the list, you can also index
new_list.pop(0)
new_list
# Quick aside, wanted to remember how to reverse a string in python
# Need to remember that slicing works like [begin:end:step]
my_string = 'hello'
my_string
my_string[::-1]
my_string
# Do lists also work this way?
my_list[::2]
my_list[::-1]
# Yup, python is beautiful
# Anyway, now showing off how to sort
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort()
num_list.sort()
# Since these are methods, they alter the object itself, it doesn't return anything
new_list
num_list
# Example of common beginner mistake
sorted_list = new_list.sort()
# It's empty, bc nothing got returned
sorted_list
type(sorted_list)
# The built in way to reverse a list
num_list.reverse()
num_list
num_list.reverse()
num_list
# Check the length
len(my_list)
 