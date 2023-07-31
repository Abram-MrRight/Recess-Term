#Tuples are used to store items in single variable
#Tuples are ordered and unchangable
phones = ("samsung", "iphone", "Techno", "samsung", "Techno")
print(phones)
#Excercise use the len() with this tuple example

#Tuple showing different data types

Tuple1 = ("matooke", "rice")
Tuple2 = (100, 200, 500)
print(Tuple1)
print(Tuple2)

#Exercise How to access tuples

#Add items to a tuple
phones = ("samsung", "iphone", "Techno", "samsung", "Techno")
z= list(phones)
z.append("nokia")
phones =tuple(z)
print(phones)

#Add two tuples together
laptops = ("Dell", "HP", "Acer")
laptop = ("samsung", )
laptops += laptop
Newstock = laptops + laptop
print(laptops)
print(laptop)
print(Newstock)
