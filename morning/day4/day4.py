

# Assignment1
# Show encapsulation with employee information to give a
# pay increamentation (salary with employee information to new salary) eg from 850000 to 100000
import math


class Employee:
    def __init__(self):
        self.employee_id = ""
        self.name = ""
        self.salary = 0

    def set_employee_info(self, employee_id, name, salary):
        self._employee_id = employee_id
        self._name = name
        self._salary = salary

    def increment_salary(self, increment_amount):
        self._salary += increment_amount

    def get_employee_details(self):
        return f"Employee ID: {self._employee_id}\nName: {self._name}\nSalary: {self._salary}"


# Create an instance of the Employee class
employee = Employee()

# Set the employee information
employee.set_employee_info("E001", "Atong Abraham", 850000)

# Increment the salary by a specific amount
increment_amount = 150000
employee.increment_salary(increment_amount)

# Retrieve and display the employee details
employee_details = employee.get_employee_details()
print(employee_details)


# Day4 Monday 26th june 2023
# Object Oriented Programming

# Key concepts
"""
1. Class
2. Object
3.Encapsulation
4.Inheritance
5.Polymorphism
6.Abstraction

"""

# Class
# A class is a blue print for creating objects
"""
class Car:
    def _init_(self, make, my_file_model, year):
        self.make = make
        self.my_file_model = my_file_model
        self.year = year

    def start_engine(self):
        print("engine started")

    def stop_engine(self):
        print("engine stopped")

    
my_car = Car("Toyota", "Corola", 2022)
print(my_car.make)
print(my_car.my_file_model)
print(my_car.year)

my_car.start_engine()
my_car.stop_engine()"""

# Bank account
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
"""
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):

        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
"""

# Example Rectangle


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Create an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Calculate and print the area
area = rectangle.calculate_area()
print("Area of the rectangle:", area)

# Calculate and print the perimeter
perimeter = rectangle.calculate_perimeter()
print("Perimeter of the rectangle:", perimeter)


# Class student
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name", self.name)
        print("Name", self.year)
        print("Name", self.course)


# Create object
my_student = Student("Jeff Geoff", 3, "Sostware Engineering")
my_student.display_details()


# class person


# Using Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name, "Im", self.age)


p1 = Person("John", 36)
p1.myfunc()


# Calculate circuference of a circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2


# Create an instance of the Circle class
circle = Circle(5)

# Calculate and print the area
area = circle.calculate_area()
print("Area of the circle:", area)


# calculate and display employee bonuses(0.5) of salary (employee1:150000, employee2:230000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def my_bonus(self):
        bonus = self.salary * 0.5  # 50% bonus
        return bonus


# Create instances of the Employee class for two employees
employee1 = Employee("Employee 1", 150000)
employee2 = Employee("Employee 2", 230000)

# Calculate and display the bonuses for each employee
print("Employee:", employee1.name)
print("Salary:", employee1.salary)
print("Bonus:", employee1.my_bonus())
print()

print("Employee:", employee2.name)
print("Salary:", employee2.salary)
print("Bonus:", employee2.my_bonus())


# Encapsulation
# Key main goals of encapsulation
"""
1. To hide the implementation detials of an object
2. To protect the object from changes   
3. To prevent
"""

# Example4: With a bank account
"""
class Bank_Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number #Encapsulation the account number
        self.balance = balance   #Encapsulation the balance

    def deposit(self, amount):
        self.balance += amount #Encapsulate deposit amount

    def withdraw(self, amount):
        self.balance -= amount #Encapsulate withdraw amount

       if self.balance >= amount:
        self.balance -= amount #Encapsulate withdraw amount
        else:
        print("Insufficient balance")
    

    def get_balance(self):
        return self.balance
    
    # Create a Bank object
bank_account = Bank_Account(123456, 10000)

    #Accessing the bank object and modify encapsulated attributes indirectly
print(bank_account.account_number)
print(bank_account.balance)
bank_account.deposit(5000)
print(bank_account.balance)
bank_account.withdraw(5000)"""


# Exercise2: Convert temperature (37 celsius) from celsius to fahrenheit

class TempConverter:
    def __init__(self):
        self.celsius = 0
        self.fahrenheit = 0

    def set_celsius(self, celsius):
        self._celsius = celsius

    def convert_to_fahrenheit(self):
        self._fahrenheit = (self._celsius * 9/5) + 32

    def get_fahrenheit(self):
        return self._fahrenheit


# Create an instance of the TemperatureConverter class
converter = TempConverter()

# Set the temperature in Celsius
converter.set_celsius(37)

# Convert the temperature to Fahrenheit
converter.convert_to_fahrenheit()

# Retrieve the converted temperature in Fahrenheit
fahrenheit = converter.get_fahrenheit()

# Print the result
print("Temperature in Celsius:", converter._celsius)
print("Temperature in Fahrenheit:", fahrenheit)
