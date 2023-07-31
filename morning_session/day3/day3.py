# DAY3

# tkinker learn 
 #Assignment: Create a simple calculator program with a GUI interface.
 #Make the title of the calculator program window with your name e.g "jeff Geoff simple calculator"


import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except Exception as e:
        output.config(text="Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("Jeff Geoff Simple Calculator")

# Create an entry field for input
entry = tk.Entry(window, width=30)
entry.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the output
output = tk.Label(window, text="Result: ")
output.pack()

# Start the main event loop
window.mainloop()





#Basic operators and expressions(input and output operation)

"""
-Arithmetic operators
+Addition
-Substraction
*Multiplication
/Division
//Divide(return quotient without remainder)
% Modulus
**Exponentiation

-Comparison Operators
==Equal to
!= Not Equal to !==
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

- Logical Operators
Logical AND 'and'
Logical OR: 'or'
Logical NOT: 'not'

-Assignment operators
 Assign value: '='
 Add value: '+'
 Add and assign value: '+='
 Substract and assign value: '-='
 Modulus and assign value: '%='
 Exponentiate and assign value: '**='


 -Membership Operators
 In: 'in' Operator: checks if a value exists in  a sequence
 Not: 'not in' operators: checks if a value doesnt exist in a sequence

 -Identity Operator:
 Is: 'is' operator: checks if two values are the same
 Is not: 'is not ' operator: checks if two values are not the same

"""

# Examples of arithmetic operators

#Arithmetic operators
#Addition
x = 50 + 45
print(x)

#Substraction
y =50 - 45
print(y)

#Multiplication
a = 50*45
print(a)

#Division
b = 50/45
print(b)

#Divide(return quotient without remainder)
d = 50//45
print(d)
#Modulus
c =50 % 45
print(c)
#Exponentiation
e = 50 ** 45
print(e)


# Comparison Operators
#Greater than
a = 15
b =9
if a > b:
 print('a is greater than b')

print(a>b)

# Less than
if b> a:
 print('b is greater than a')

print(a>b)
 
#Greater tha or equal to
if a>= b:
 print('a is greater than or equal to b')

print(a>= b)

#Less than or equal to
if b<= a:
 print("--------------------------")
 print('b is less than or equals a')

print(a<=b)
print("--------------------------")

#Equal to

if b == a:
 print('b is equal to a')

print(a==b)

# Logical Operators
# Examples

a = True
b = False

# Logical AND
print(a and b)

# Logical OR
print(a or b)

# LogicalNOT
print(not b)
print(not a)


# Assignment Operators
# Compound assignment operators
a = 5
# Add and assign
a += 5
print(a)

#  substract and assign
b = 19
b -= 5
print(b)

 # multiply and assign
c = 10
c*=5
print(c)

# Dividey and assign
d= 10
d/=5
print(d)

# Modulus and assign
e = 10
e%=5
print(e)

# Exponentiation and assign
f = 10
f**=5
print(f)

# Membership assignment operators

cars = ['Jeep', 'Telsa', 'BMW', 'Roll Royce']
if 'Jeep' in cars:
 print('Jeep is in the list')
 print('Telsa ' in cars)
 print('Toyota ' in cars)

 # Identity Operators
 x =10
 y =10

 # Is Operator
print(x is y)
print(x is not y)
print(x == y)
print(x != y)
print(x < y)
print(x <= y)

#List 
z = [1,2,3,4,5,6, 7]
w = [1,2,3,4,5,6, 7]

print(z is w)

"""
#Btwise operators
# Bitwise operators are used to perform operations individuals bits in of binary numbers
Bitwise AND (&): performs bitwise AND operation between corresponding bits of two integers
Bitwise OR(|) performs bitwise OR operation btn corresponding bits of two integers
Bitwise XOR(^) performs bitwise XOR operaion

"""
#Examples of Bitwise operations
a = 10
b = 20
#Bitwise AND operation
result = a & b
print(result)

#Bit
#Example and Assignment
# Create a simple calculator to calculate (add, substract, multiply, divide)

def add(a, b):
 return a +b
def substract(a, b):
 return a -b
def divide(a, b):
 return a / b
def multiply(a, b):
 return a * b

def main():
 print('Jeff simple calculator')
number1 = float(input("Enter the first number"))
number2 = float(input("Enter the second number"))
operator = input("Enter the operator(+, -, *, /:)")

if operator == '*':
 result = add(number1, number2)
elif operator == '-':
 result = substract(number1, number2)
elif operator == '*':
 result = multiply(number1, number2)
elif operator == '/':
 result = divide(number1, number2)
else:
  print('Invalid operator') 
  #  return
print("The result is", result)
if __name__ == '_main_':
 main()

 