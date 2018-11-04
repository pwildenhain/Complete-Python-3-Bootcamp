# While loops work off of boolean logic
# haha, first time I did this I forgot to add x+= 1 and created
# an infinite loop. In the terminal I can use ctrl + c to interrupt
x = 0
while x < 5:
    print(f'the current value of x is : {x}')
    x += 1
# We can also use the else statement in a while loop as
# a kind of shorthand for the if-else logic
# basically if there is only one other option you don't need
# an if-else in a while loop, you can just use an else
x = 0
while x < 5:
    print(f'the current value of x is : {x}')
    x += 1
else:
    print('x is too big now')
# this can also be used in for loops. seems like a sleeker
# more concise way to add a conditional. Something that you 
# always want to execute at the end of a loop, or that you want to 
# execute if you don't meet the condition for a while loop. Again, 
# a better way to do simple conditionals with loops

# Now learning about loop keywords: break, continue, and pass

# pass is a great placeholder to ensure that your loops still run, 
# without having to commit to doing anything yet

x = [1, 2, 3]

for num in x:
    pass

print('I will get back to this')

# continue will take you back to the top of the current closest enclosing loop

name = 'Wildenhain'
# When this comes to a h, it will skip the rest of the loop and go back to 
# the top
for char in name:
    if char == 'h':
        continue
    print(char)
# break will bust out of the current closest loop, and stop executing that loop
for char in name:
    if char == 'h':
        break
    print(char)





