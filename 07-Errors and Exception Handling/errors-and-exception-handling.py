# Without error handling, the entire script gets aborted when an error is found
# With error handling, we can alert the user of the error, and continue to run the script

# try - except- finally is the trifecta of exception handling
# try
# Try to execute this code
# except
# Run this code if you hit an error
# else
# Do this code after we are sure there are no errors
# finally
# Always run this code after everything is said and done

# Take a simple function as an example


def add(a, b):
    print(a + b)


add(1, 2)
print("Good Job")
# But what if someone uses it the wrong way?
# We get a TypeError, and no further code is executed
add("1", 1)
print("Good Answer")

# Simple try block

try:
    result = 1 + 1
except:
    print("Don't you know how to add?")
else:
    print(result)
    print("Good job adding")
finally:
    print("Ok now we are done")

try:
    result = "1" + 1
except:
    print("Don't you know how to add?")


# Example of opening and writing a file
# Good example of using multiple exceptions in the same try block

try:
    file = open("testfile", "r")
    file.write("Test Test Test Test")
except TypeError:
    print("there was a type error")
except OSError:
    print("*Wag Finger* You don't have permission to do that!")
finally:
    print("Alllll done")


def ask_for_int(x):
    while True:
        try:
            result = int(input("Please enter a number: "))
        except:
            print("That's not an integer!")
        else:
            print(result)
            print("Thank you")
            break
        finally:
            print("The End")
