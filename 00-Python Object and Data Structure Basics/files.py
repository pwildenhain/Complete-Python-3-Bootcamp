# Start accessing a file
myfile = open('00-Python Object and Data Structure Basics/test.txt')
# This is throw an file not found error
myfile = open('does-not-exist.txt')
# read the contents of the current file as a single string
myfile.read()
# If you run this again, it will return an empty string
myfile.read()
# this happens because when you read the first time, there is a cursor
# that goes from the beginning to the end of the file. From the 
# cursor's point of view, there is nothing to read because it's at the 
# end of the file. As long as it's open, it's actively in the file
# and I'm just directing it around
# I need to tell the cursor to go back to the beginning if I want to 
# read it again. this will return the position it lands at
myfile.seek(0)
# Now we're back at the beginning
myfile.read()
# You can also limit how many characters from the file you read
myfile.seek(0)
myfile.read(5)
# Save the output to a variable
myfile.seek(0)
content = myfile.read()
# This will just be a giant string which isn't always useful
# We can use readlines to read each line as an element in a list
myfile.seek(0)
content_list = myfile.readlines()
content_list
# again, this will push us to the end of the file
myfile.read()
# so we need to reset it again if we want it to be useful
myfile.seek(0)
# lastly, we need to remember to close a file when we're done with it
# Or else we'll get errors if we try to manipulate the file and save it
myfile.close()
# A good way to avoid this scenario is to use the with statement
with open('00-Python Object and Data Structure Basics/test.txt') as myfile:
    with_content = myfile.read()
# This automatically closes the file for us, and we still have access to content
with_content
# We can also set the permissions for what the open is allowed to do
# with the mode parameter. the default value is r which stands for read
with open('00-Python Object and Data Structure Basics/test.txt', mode = 'r') as myfile:
    read_content = myfile.read()
read_content
# If we set the permissions to write only, and we try to read, we'll get a
# 'not readable' error
with open('00-Python Object and Data Structure Basics/test.txt', mode = 'w') as myfile:
    read_content = myfile.read()
# Different modes
# r == read only
# w == write only, overwrite existing or create a new file
# a == append only
# r+ == reading and writing
# w+ == writing and reading (to overwrite existing, or create a new file) 

# Create a new file. This will return however many characters were written
with open(
    '00-Python Object and Data Structure Basics/newfile.txt',
    mode = 'w'
    ) as newfile:
    newfile.write('FIRST on ONE\nSECOND on TWO\nTHIRD on THREE')   

# And now I have a new file to play around with!
with open(
    '00-Python Object and Data Structure Basics/newfile.txt',
    mode = 'r'
    ) as newfile:
    mynewfile = newfile.read() 
mynewfile 
# append another line to this new file
with open(
    '00-Python Object and Data Structure Basics/newfile.txt',
    mode = 'a'
    ) as newfile:
    newfile.write('FOURTH ON FOUR')
# good to see that it doesn't auto write it to a new line. I bet write lines does that
with open(
    '00-Python Object and Data Structure Basics/newfile.txt',
    mode = 'r'
    ) as newfile:
    newfile.read()
# try out writelines
with open('00-Python Object and Data Structure Basics/newfile.txt', mode = 'a') as newfile:
    newfile.writelines('FIFTH on FIVE')
# huh, it doesn't add a new line automatically. prob needs a list
with open('00-Python Object and Data Structure Basics/newfile.txt', mode = 'r') as newfile:
    newfile.read()




