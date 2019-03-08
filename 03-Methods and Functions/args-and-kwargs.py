# *args == arguments
# **kwargs == keyword arguments
# Simple function, with positional arguments - AKA each position has a specific assignment
# In the example below a is 50, because it's in the same position
def five_percent_of_two_sum(a, b):
    return sum((a, b)) * 0.05

five_percent_of_two_sum(50, 50)    
# Great, but what if I need to add more numbers?
# I can use *args, which will pass the variable
# args into my function as a tuple
def five_percent_of_any_sum(*args):
    return sum(args) * 0.05

five_percent_of_any_sum(20, 20, 20, 10, 10, 10, 10)

# *args is an arbitrary choice, it could be anything

def show_me_spam(*spam):
    print(spam)

show_me_spam('spam', 'spam', 'spam')

# If it matters what they are specifying, I can use **kwargs for
# keyword arguments, which puts kwargs into my function as a 
# dictionary

def rich_or_poor(**kwargs):
    if 'money' in kwargs:
        print(f"You are rich, you have ${kwargs['money']}")
    else:
        print('Sorry you are poor')

rich_or_poor(love = 'yes')
rich_or_poor(money = 10)

# Again, kwargs is just standard style, it's the "**" that matters

# We can use them both together to cool effect
def grocery_list(*args, **kwargs):
    """
    Given line item prices, and categories of object, nicely print
    the grocery_list
    """
    for category, things in kwargs.items():
        print(f"{category}:\n{', '.join(things)}")
    print(f'Total cost: ${sum(args)}')


grocery_list(10, 12, 30, 15, 12, fruits = ["apple", "banana"], meats = ["pork", "chicken"])

# function from exercise
def myfunc(s):
    s_weird = ''
    for i, l in enumerate(s):
        if i % 2 == 0:
            s_weird += l.lower()
        else:
            s_weird += l.upper()
    return s_weird

myfunc('Anthropomorphism')
test_s = 'Anthropomorphism'
for i, l in enumerate(test_s):
    print(f'{l}: {i}')



