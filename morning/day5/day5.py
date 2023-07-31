
#Assignment 1 : Deadline 01 July 2023 Time 5:00PM EAT
# # Create a receipt printing program with GUI interface, 
# # a more advanced detail earns you more points.


from tkinter import *

root = Tk()
root.geometry("300x100")


def show_receipt():
    top = Toplevel(root)
    top.geometry("300x200")
    top.configure(background="white")

    prices = [100, 200]
    quantities = [2, 1]
    totals = [price * qty for price, qty in zip(prices, quantities)]

    heading = Label(top, text="--- RECEIPT ---", bg="blue")
    heading.pack()

    table_heading = Label(top, text="PRICE\tQUANTITY\tTOTAL", bg="red")
    table_heading.pack()

    for price, qty, total in zip(prices, quantities, totals):
        item_label = Label(top, text=f"{price}\t{qty}\t{total}", bg="white")
        item_label.pack()

    total_label = Label(top, text=f"Total: {sum(totals)}", bg="red")
    total_label.pack()


button = Button(root, text="Generate Receipt", command=show_receipt, bg="blue")
button.pack(padx=10, pady=10)

root.mainloop()










# Exercise1
# Demonstrate using inheritance to calculate area and parameter of circlee and rectangular respectively
# Base class(shape:circle, rectangle)
class Shape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print(self.radius)

# Derived class(circle, rectangle)


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, radius)

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print(self.radius)
        print(self.area())
        print(self.perimeter())


class Rectangle(Shape):
    def __init__(self, width, length):
        Shape.__init__(self, width)
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def display(self):
        print(self.width)
        print(self.length)
        print(self.area())
        print(self.perimeter())


circle = Circle(5)
circle.display()

rectangle = Rectangle(10, 20)
rectangle.display()


#Multiple Inher
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

class Dog(Animal):
  def bar(self):
      print(self.name + " is barking")

class Cat(Animal):
    def meow(self):
        print(self.name + " is meowing")

def display_info(self):
    print(self.name)


#create objects
animal = Animal("Animal")
dog = Dog("Spot")
cat = Cat("Fluffy")

#calling functions
animal.eat()
dog.eat()
dog.eat()
print("--------------------------------")


#Polymorphism
#method overloading
#method overriding

#method overloading
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
            self.length = length
            self.width = width

    def calculate_area(self):
        return self.width * self.length
    
    def display(self):
        print(self.length)
        print(self.width)
        print(self.calculate_area())



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
     return 3.14 * self.radius * self.radius
    
    def display(self):
        print(self.radius)
        print(self.calculate_area())


#create objects
rectangle = Rectangle(10, 20)
circle = Circle(5)

#calling functions
rectangle.calculate_area()
circle.calculate_area()
rectangle.display()
circle.display()
print("method overloading---------------------")


# method overriding
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.width * self.length
    
    def display(self):
        print(self.length)
        print(self.width)
        print(self.calculate_area())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def display(self):
        print(self.radius)
        print(self.calculate_area())

rectangle = Rectangle(10, 20)
circle = Circle(5)

rectangle.display()

circle.display()
print("method overriding-------------------")

    



#Abstraction 
#Example5:Demonstraction abstractions

class Vehicle(object):
    pass


class Car(object):

    def stop(self):
        print("Stopping the truck")

class Truck(Vehicle):
    def stop(self):
        print("Stopping the truck")



#Exercise2 Demonstrate abstraction using calculating area of a circle and rectangle
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
print("Area of Circle:", circle.area())

rectangle = Rectangle(4, 6)
print("Area of Rectangle:", rectangle.area())




#Notes
# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")


class Dog(Animal):
    def bar(self):
        print(self.name + " is barking")


class Cat(Animal):
    def meow(self):
        print(self.name + " is meowing")


# create Animal object
animal = Animal("Animal")
dog = Dog("Spot")
cat = Cat("Fluffy")

# Invoke Eat
animal.eat()
dog.eat()
dog.eat()
print("--------------------------------")


# to demonstrate how parent constructors are called.
# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()


# example2 Demonstrating inheritance
class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def accelerate(self):
        self.speed = self.speed + 1

    def brake(self):
        self.speed = self.speed - 1


class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.color = "red"
        self.wheels = 4

    def display(self):
        print(self.name)
        print(self.speed)
        print(self.color)
        print(self.wheels)


car = Car("BMW")
car.accelerate()
car.brake()
car.display()
print("--------------------------------")

