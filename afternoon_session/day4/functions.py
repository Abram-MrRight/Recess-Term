
#functions
# Arguments(Atong, Abraham)
#Parameters(fname, lname)

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Atong", "Abraham")



# Arbitrary Arguments, *args
#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Thomas", "John", "Abraham")


#You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#If the number of keyword arguments is unknown, add a double ** before the parameter name
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Aliasing in Python
first_variable = "PYTHON"
print("Value of first:", first_variable)
print("Reference of first:", id(first_variable))

print("--------------")

second_variable = first_variable # making an alias
print("Value of second:", second_variable)
print("Reference of second:", id(second_variable))


#it is clear that first_variable and second_variable have the same reference id in memory.
"""
Value of first_variable: PYTHON
Reference of first_variable: 2904215383152
--------------
Value of second_variable: PYTHON
Reference of second_variable: 2904215383152
"""