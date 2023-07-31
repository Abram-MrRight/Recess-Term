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



