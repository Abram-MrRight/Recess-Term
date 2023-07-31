# DAY 06
# Advanced topics in python

"""
*Regural expressions
*Generators and iterators
*Decorators
*context managers
*Multithreading and multiprocessing

NB: Next wednesday data science(data virstualization)
#.ipynb for jupyter notebook
#(thurday, numpy & pandas)

"""

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
"""
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string

Regular expressions
\d:Matches a string with a number of characters separated by spaces 
\w:Matches a string with a word character 
\s:Matches a string with a whitespace character
\D:Matches a string with a non-digit character
\W:Matches a string with a non-word character
\S:Matches a string with a non-whitespace character
\A:Matches the beginning of a string
\Z:Matches the end of a string

"""

# 1. Regural expressions
# Matching and Searching
# regex, re.match(), re.search(), re.findall()

# Example1
# Demonstrateing regex | match first word, match Group word, match All Number


import re
text = "Hello, my name is Abraham Atong . Im a programmer with 15years of experience"

# match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Matches:", match.group())


matches = re.findall(r"\d+", text)
print("Matches:", matches)
print("----------------------------------------------------------------")


# Example2: Validate email address


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+\w+$'

    if re.match(pattern, email):
        return True
    else:
        return False

    # Example usage
email1 = "atongkurabraham@gmail.com"
email2 = "atongkurabraham@gmailcom"

print(validate_email(email1))
print(validate_email(email2))
print("----------------------------------------------------------------")



# Use regurlar expression to validate paSSWORD
import re

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if re.match(pattern, password):
        print("Valid password")
    else:
        print("Invalid password")
    print("----------------------------------------------------------------")

# Test the password validation
password1 = "Abc123@"
validate_password(password1)  # Valid password

password2 = "abc123"
validate_password(password2)  # Invalid password


# 2. Generators and Iterators
# yield generator
# Iterator '--iter--' "--next--"


def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))
print("----------------------------------------------------------------")


# Example3
# Generate function that yields the square of numbers from 1 to 10

def square_generator():
    for num in range(1, 11):
        yield num ** 2


# Using the generator function
for square in square_generator():
    print(square)
    print("----------------------------------------------------------------")



# Generate function for the square of numbers from 1 to 10 with Iterators

class SquareIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            square = self.start ** 2
            self.start += 1
            return square
        else:
            raise StopIteration


# 4. Decorators
# Decoratos allow you to modify the behavior of functions or classes without directly changing the behavior
# '@decorator_name' is the name of decorator


def my_decorator(func):
    def inner():
        print("This is decorator")
        func()
    return func


@my_decorator
def outer_decorator():
    print("This is outer decorator")
    print("----------------------------------------------------------------")


outer_decorator()


# Example2


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Code to be executed before the orignal function
        print("This is my decorator befor function execution")
        result = func(*args, **kwargs)
        print("After function execution")
    # Code to be executed after the orignal function
        return result
    return wrapper

@my_decorator
def my_function():
    print("Inside the function")
    print("----------------------------------------------------------------")

my_function()


#Example3
def my_decorator(cls):
    class ModifiedClass:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
        
        def my_method(self):
            print("modified method")

    return ModifiedClass

@my_decorator
class MyClass :
   def my_method(self):
        print("My original method")
        print("----------------------------------------------------------------")


my_instance = MyClass()
my_instance.my_method()

