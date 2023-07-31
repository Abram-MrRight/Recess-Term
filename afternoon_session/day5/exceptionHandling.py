


#Exception Handling in python

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
        name = input('enter your name: ')
        age = int(input('enter your age: '))
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

