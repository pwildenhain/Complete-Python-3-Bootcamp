# Inheritance is when you pass the attributes and methods of one object to another object
# Make code simpler and more repeatable/modular

# Create a "base" class, AKA the class to be inherited by another more specific class
class Mammal():

    def __init__(self):
        print("Mammal Created")
    
    
    def who_am_i(self):
        print("I am a mammal")

    def eat(self):
        print("I am eating")


# init method is automatically executed when object is initialized

mymammal = Mammal()

mymammal.eat()

mymammal.who_am_i()


# The features and methods in the Mammal class could be useful for the previous Dog class that we created

# This is a derived class, because it's deriving attributes from a more general "base" class

class Dog(Mammal):

    def __init__(self):
        # Initialize an Mammal class in the Dog class
        # We don't have to do this, it's just used as an example here
        Mammal.__init__(self)
        print("Dog created")

    # We can always overwrite a base class method by redefining it in our derived class
    def who_am_i(self):
        print("I am a dog")

    # We can also define our own derived class specific methods
    def bark(self):
        print("WOOF!")


# Mammal class is created first, then Dog
mydog = Dog()

# We have the Mammal methods without having to redefine them
mydog.eat()
# We also have our own methods including overwriting previous ones
mydog.who_am_i()
mydog.bark()
# This is is probably the more common way that inheritance is used. In my payday_budget
# I made an attribute of my Budget class equal to the Account class. Curious what that is called

###### Polymorphism
# Refers to how different object classes can share the same method name
# and those methods can be called from the same place even though a variety
# of objects might be passed in

class Bird():
        
    def __init__(self, name:str):
        self.name = name

    def speak(self):
        return self.name + " says cheep!"

mybird = Bird(name = "Tweety")

mybird.speak()

class Cat():
        
    def __init__(self, name:str):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

mycat = Cat(name = "Frisky")

mycat.speak()

# The speak method here is unique to each object
# We can see polymorphism at work in a for loop

for pet in [mybird, mycat]:
    print(type(pet))
    # Same method, different results
    pet.speak()


# Can also see this at work inside a function
# the method behaves differently depending on the class that it passed to it
def pet_speak(pet):
    return pet.speak() 

pet_speak(mybird)

# It seems to all boil down to having shared methods across classes
# and the implications of what you can do with that
# Executing function with method call, iterating through potentially
# wildy different objects, but with at least one shared method you can still
# do programmatic tasks with them 

# this sort of reminds me of S3 classes in R -- performing different operations
# depending on what is passed


# A common use of this is to use Abstract classes with inheritance
# Abstract class = class that you never expect to call, only to use as a base class

class Animal():

    def __init__(self, name):
        self.name = name

    # We don't ever expect someone to create and Animal object
    # So if they try to call speak on just a plain animal, we let them know
    # that they need to define speak for their specific class
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

myanimal = Animal("Bob")
# Let the user know that it's not meant to be used this way
myanimal.speak()

# It's actually meant to be used this way

class Cow(Animal):

    def speak(self):
        return self.name + " says Moo!"


betsy = Cow("Betsy")

betsy.speak()

class Sheep(Animal):

    def speak(self):
        return self.name + " says Baa!"


harry = Sheep("Harry")

harry.speak()