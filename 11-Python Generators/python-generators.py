# Regular functions have a "return" value
# Generator functions send a value, and also remember where they left off
#
# Generators allow us to create a sequence of values _over time_
# rather than having to create it and hold it in memory
#
# The main difference in syntax is the `yield` keyword
# Generator functions produce something to be iterated on
# and resume wherever the last iteration left off
#
# Think of the `range()` function. It doesn't create a list
# in memory, it just keeps track of the last number called,
# and the step size, to produce the next number in the iterable
#
# THATS why they are called generators -- given the current input
# and where they last left off, the generate just the **needed* value


# Creating an iterable the non-generator way

from typing import Generator


def create_cubes(n: int) -> list:
    """Return a list of cubes up to n"""
    return [x ** 3 for x in range(n + 1)]


create_cubes(3)

for idx, cube in enumerate(create_cubes(10)):
    print(f"The cube of {idx} is: {cube}")

# Notice for this example, we don't need the entire list in memory,
# since we're only accessing one value at a time -- this is where generators come in


def generate_cubes(n: int) -> Generator[int, None, None]:
    """Provide a generator of all the cubes up to n"""
    for x in range(n + 1):
        yield x ** 3


# No longer a list, but an object in memory
generate_cubes(3)

for idx, cube in enumerate(generate_cubes(10)):
    print(f"The cube of {idx} is: {cube}")

# Fibonnaci sequence example
# Good example of doing things _after_ yielding -- which can't be done after a regular function
def fibonnaci(n: int) -> Generator[int, None, None]:
    """Generate the fibonacci sequence up until n"""
    first = 1
    second = 1
    for _ in range(n):
        yield first
        first, second = second, first + second


list(fibonnaci(10))

# The key to understanding generators is the next and iter functions

fib_10 = fibonnaci(10)

fib_10
# Manually gext the next generator value
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
next(fib_10)
# Once we've exhausted the generator, it will raise a StopIteration exception
next(fib_10)

# Now for iter(), take a string

s = "hello"
# We can iterate over it
[char for char in s]
# But for some reason next(s) tells us it's not an iterator
next(s)
# so it supports iteration, but it not an iterator -- let's fix that
s_iter = iter(s)

next(s_iter)
next(s_iter)
# So iter converts an _iterable_ into an _iterator_ i.e like a generator
s_iter

# homework

# Problem 1
# Create a generator that generates the squares of numbers up to some number N.

def gensquares(n):
    for x in range(n):
        yield x ** 2

for x in gensquares(10):
    print(x)


# Problem 2

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:


from random import randint

def rand_nums(low, high, n):
    for _ in range(n):
        yield randint(low, high)

for num in rand_nums(low=1, high=10, n=12):
    print(num)



# Problem 4

# Explain a use case for a generator using a yield statement
# where you would not want to use a normal function with a return statement.

# You would want to use a generator instead of normal function if you needed to
# create a large list, but didn't need to access all of the list at once. A generator
# will allow you to iterate through the data, without hogging the memory to
# keep it there.


# Extra Credit!

# Can you explain what gencomp is in the code below?
# (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)



my_list = [1,2,3,4,5]
# Generator comprehensions might be the way to go!
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
#####
# Seems to be a generator
type(gencomp)
# Raise StopIteration like a generator would
next(gencomp)

