# Learning about control flow; using logic to execute code only when we want to
# Keywords if, elif, else and all of these make use of indentation in it's control flow
if True:
    print('ITS TRUE!')
# We'll be using this with comparisons and variables
hungry = True
if hungry:
    print('FEED ME')
# Handling other conditions
burgers_left = -2
if burgers_left >= 1:
    print('FEED ME')
elif burgers_left == 0:
    print('time for a nap')
else:
    print('How do I have negative burgers??')
    