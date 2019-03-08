# A method is a function that is built into an object
mylist = [1, 2, 3]
# Examples of methods
mylist.append(4)
mylist
mylist.reverse()
# Get info on methods
help(mylist.reverse)
# Explore documentation at docs.python.org, check out standard library

# Bolierplate function

def name_of_function(param):
    """
    Docstring explains function purpose/parameters
    """
    # Perform the task
    greeting = 'Hello ' + param 
    # Return a value
    return greeting

name_of_function('Paul')
# See the docstring I created
help(name_of_function)

def print_hello(name):
    print('hello ' + name)

print_hello('Paul')

# Since we're printing, the function doesn't actually return anything
#pylint throws an error, for this line, well done!
#result = print_hello('Paul')
#result
#type(result)
# If we want to save the output, we have to return it
def say_hello(name):
    return 'hello ' + name

result = say_hello('Paul')
result

# functions help solve problems
# Problem one, see if the word dog is in a string
# Original version
def find_dog(word:str):
   return True if word.find('dog') > -1 else False

find_dog('I love my cat')
find_dog('I love my hotdog')
find_dog('DOGS are great')

# A better, non-beginner version
# Use in, it's simpler
# Return the boolean value, no need to return True or False
def find_dog_better(word:str):
   return 'dog' in word.lower()

# Problem two, translate a word into pig latin
# If word starts with a vowel, add 'ay' to the end
# Otherwise, take the first letter, and add it to the 
# end along with 'ay'

def pig_latin(word:str):
    """
    Translate a word into pig latin
    """
    word = word.lower()
    first_letter = word[0]
    if first_letter in ['a', 'e', 'i', 'o', 'u']:
        return word + 'ay'
    else:
        return word[1:] + first_letter + 'ay'

pig_latin('python')
# Better version
# don't forget that a string is a simple data structure, and an iterable!
# Assign to a variable, and then just return that variable, it's more readable
def pig_latin_better(word:str):
    """
    Translate a word into pig latin
    """
    word = word.lower()
    first_letter = word[0]
    
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word
