

# input and output in python
# input('prompt)
# Example of input

name = input("Enter your name: ")
print("My name is, ", name)

number = int(input("Number"))
product = number *10
print(product)


# How to capture the input from tuple
w = (2, 3, 4, 5, 6)
print("Current tuple")
print(w)
print(type(w))


E = list(w)
E.append(int(input("Enter the new values: ")))

w = tuple(E)
print("updated tuple")
print(w)

myList = list(map(int, input("Enter the list values: ").split()))
myset = set(map(int, input("Enter the values").split()))

print(myList)
print(type(myList))
print(myset)
print(type(myset))

s, r, w = map(int, input("Enter the values: ").split())
print("The values are: ", end=" ")
print(s, r, w)

