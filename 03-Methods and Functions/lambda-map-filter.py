# Example function to use with map()

def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

# A couple ways to get the square of these numbers

# for loop
my_squares = []
for num in my_nums:
    my_squares.append(square(num))

my_squares

# list comprehension
my_squares = [square(num) for num in my_nums]
my_squares

# and mapping
my_squares = list(map(square, my_nums))
my_squares

# No need to call the function
# within map (ie func not func())

# filter function
# All filter functions need to either 
# return True or False

def check_even(num):
    return num % 2 == 0

check_even(3)

my_nums = [1, 2, 3, 4, 5]
list(filter(check_even, my_nums))

# these short little functions really didn't
# need to exist on their own, which is 
# why we have lambda expressions 
# no need for def, a name, and no need for the 
# return keyword, since it's an 
# anynomous function

list(map(lambda num: num ** 2, my_nums))
# everything is defined succinctly 



