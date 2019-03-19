# Creating object thats have their own methods and attributes
# Use information about the object, or the object itself
    # to return information, or alter the existing object
# Enables code to be repeatable and organized

# Define an object by using the class keyword, with CamelCase
# come with an __init__ method that gets called when an instance
# of the class is created

# An example of creating an instance of an object

my_set = set()
# Calling the pop method on the set object
my_set.pop()
# EVERYTHING in python is an object
type(my_set)
# my_set is an instance of the set class/object

# Simplest class
class Sample():
    pass

my_sample = Sample()

type(my_sample)

class Dog():
    """A Dog object"""
    def __init__(self, breed:str, name:str, spots:bool):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = 'Bernese Mountain', name = 'Richard', spots = False)

# Now the my_dog instance has attributes saved inside of it
my_dog.breed
my_dog.name
my_dog.spots

# the self keyword tells python that this is something particular 
# to the class
# also "self" is just a convention, but one that should be adhered to
# and following that, self.breed, could be any attribute, but by convention
# it should be named after the __init__ parameter that it's connected to

# Looks like duck typing doesn't do any good for preventing type errors
# but, VS code does throw an error (pylint)
your_dog = Dog(breed = 'Husky', name = 'Jonathon', spots = 'No')
your_dog.spots
