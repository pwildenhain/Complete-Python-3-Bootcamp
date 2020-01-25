# Function review
# a simple function
def one():
    return 1


one()
# The function is an object
one
# Which can be assigned to another object
one_again = one
# and called
one_again()
# Is one_again() a copy of one()? Or is it just pointing to it?
# Let's try deleting it and seeing
del one
one_again()
# Looks like it copies, not just points to it :-O
# let's see how passing functions to other functions works
def first():
    print("The first() func has started")
    
    def second():
        return "\t This is the second() func inside first()"
    
    def third():
        return "\t This is the third() func inside first()"

    print(second())
    print(third())

    print("The first() func has ended")


first()

# We can't use second or third since their scoped to just first(), but we can make it so that 
# we return the functions themselves

def pet_sound(pet="dog"):

    def dog_sound():
        print("woof")

    def cat_sound():
        print("meow")

    return dog_sound if pet == "dog" else cat_sound


sound = pet_sound()

sound()

sound = pet_sound(pet="cat")

sound()
# It's pointing to the cat_sound function _inside_ of pet_sound -- cool
sound

# now we want to pass in a function as an argument

def word_from_sponsors():
    return "But first, a word from our sponsors"

def do_something(do_first_func):
    print("I am doing something important")
    print(do_first_func())
    print("I'm done doing something")

do_something(do_first_func=word_from_sponsors)

# now we have the tools we need to make a decorator
from random import randint

def give_lucky_numbers(func: callable) -> callable:
    """Decorator that gives the lucky numbers after a function is called"""

    def wrapper():
        func()
        lucky_nums = [str(randint(1, 100)) for _ in range(6)]
        print(f"Your lucky numbers are: {', '.join(lucky_nums)}")

    return wrapper

# def do_business():
#     print("I am doing a business")

# We can use this decorator to help us create a new function
lucky_business = give_lucky_numbers(do_business)

lucky_business()

del lucky_business
# Or we can use this super slick syntax
@give_lucky_numbers
def do_business():
    print("I am doing a business")


do_business()

