
#1. FILE HANDLING
#2. EXCEPTION HANDLING 




#1. FILE HANDLING

# The key function for working with files in Python is the open(), close() function.

"""
----File Modes-----

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


you can specify if the file should be handled as binary or text mode
-"t" - Text - Default value. Text mode

-"b" - Binary - Binary mode (e.g. images)
"""



# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Hello! Welcome to demofile.txt. Good Luck!\n")
f.write("This file is for testing purposes. \n")
f.write("Good Luck!!")

f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
print("--------------------------------")

# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
print("--------------------------------")




# If the file is located in a different location, you will have to specify the file path, like this:
# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())


# Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))
f.close()
print("--------------------------------")


# Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())
f.close()
print("--------------------------------")


# Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()
print("--------------------------------")


# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
    print(x)
f.close()
print("--------------------------------")



# Remove the file "demofile.txt":

# os.remove("demofile.txt")


# Check if file exists, then delete it:

# if os.path.exists("demofile.txt"):
# os.remove("demofile.txt")
# else:
# print("The file does not exist")

# Remove the folder "myfolder":

# os.rmdir("myfolder")






#2. Exception Handling in python

a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))

    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")




# Program to handle multiple errors with one
# except statement

def fun(a):
    if a < 4:

        # throws ZeroDivisionError for a = 3
        b = a/(a-3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)


except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")




# Program to depict else clause with try-except

def calculate(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
calculate(2.0, 3.0)
calculate(3.0, 3.0)




# Python program to demonstrate finally
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

print("--------------------------------")



# Custom exception

class UnderAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ZeroAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def hotel():
    try:
        name = "Abraham"
        age = 23
        if (age <= 0):
            raise ZeroAgeError('Age can not be zero or less')

        elif (age < 18):
            raise UnderAgeError('You are under age')
        else:
            print(f'{name} youre welcome')
    except UnderAgeError as e:
        print(e)
    except ZeroAgeError as e:
        print(e)
    except TypeError:
        print('Error')
    else:
        print(f'{name} you are welcome to our hotel')
    finally:
        print('thanks for comming')


hotel()






