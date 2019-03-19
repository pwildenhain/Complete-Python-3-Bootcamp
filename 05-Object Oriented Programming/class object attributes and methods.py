class Dog():
    """its a dog"""

    # we can define class atrributes, that are the same for every instance
    # of a class
    # we don't need a self keyword, since that refers to a particular instance
    # of the Dog class, and this attribute will be the same for all dogs

    go_to_heaven = True

    def __init__(self, breed:str, name:str, spots:bool):
        self.breed = breed
        self.name = name
        self.spots = spots
    def bark(self, number:int):
        for bark in range(number):
            print(f'BARK! My name is {self.name}')
doggo = Dog(breed = 'german shepherd', name = 'charlie', spots = True)
# will always be True, I don't need to define it
doggo.go_to_heaven
# Using the method we define
doggo.bark(5)
# good boy


class Circle():

    pi = 3.14

    def __init__(self, radius:float = 1):
        self.radius = radius
        # doesn't need to be defined by a parameter
        # still need to use the Circle keyword for the pi
        # class attribute
        self.area = radius**2*Circle.pi
    
    def get_circumference(self):
        return self.radius * Circle.pi * 2
# Don't need to specify with default parameter
my_circle = Circle()

my_circle.get_circumference()
# Can override the default value
your_circle = Circle(30)

your_circle.get_circumference()

your_circle.area