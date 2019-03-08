# Learning about scope and how variables are 
# stored
x = 25

def printer():
    x = 50
    return x
# This will return 50, because that is what x
# is assigned in the function scope
printer()
# But this will return 25, because that is
# x is defined in the global scope
x

# Important scope rule : LEGB 
# L: Local - names assigned within a function 
# E: Enclosing function locals: names assigned 
#    within all enclosing functions from
#    inner to outer 
# G: Global Names assigned at the top-level 
#    of a module file, or declared global 
#    within a function def 
# B: Built-in, preassigned python names, ie 
#    map, range, str, print
# Python searches for variables in this order, 
# from top to bottom

# Example of local
# the num variable is scoped only to this 
# lambda function
lambda num: num ** 2

# Example of Enclosing function local
# Notice how my name variable, can be accessed
# by and enclosing function, since name is
# not defined in hello() local namespace
def greet():
    name = 'Paul'

    def hello():
        print('Hello ' + name)

    hello()

greet()

# Example of Global. Python now looks all the
# way back to my global environment to find
# the name variable, since it doesn't exist
# in the local, or the enclosing local 
# namespace

name = 'Bre'

def greet():

    def hello():
        print('Hello ' + name)

    hello()

greet()

# example of built-in
# even though I haven't defined len, I can still
# call it, because it's in the python built-in
# namespace
len

# Displaying how to use the global key work

x = 50

def local_ex(x):
    print(f'x is {x}')
    # local reassignment
    x = 25
    print(f'x is now {x}')

# prints 50
x
local_ex(x)
# still 50, because we only changed scope
# locally
x

def global_ex():
    # Let this function know that we want to 
    # use and manipulate the value of x
    # from the global scope
    global x
    print(f'x is {x}')
    # local reassignment, on a global variable
    x = 25
    print(f'x is now {x}')

# prints 50
x
global_ex()
# now will print 25, since we gave it permission
# to go up to the global scope
x

# In general, this path of global variables is
# not reccommended