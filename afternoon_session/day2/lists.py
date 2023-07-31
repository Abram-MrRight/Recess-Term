
#my research
my_list = [1, 2, 3, 4, 5]

# Accessing individual elements
print(my_list[0])   # Output: 1
print(my_list[2])   # Output: 3

# Negative indexing (accessing elements from the end of the list)
print(my_list[-1])  # Output: 5
print(my_list[-3])  # Output: 3

# Slicing a list
print(my_list[1:4])   # Output: [2, 3, 4]
print(my_list[:3])    # Output: [1, 2, 3]
print(my_list[2:])    # Output: [3, 4, 5]
print(my_list[::2])   # Output: [1, 3, 5]
print(my_list[::-1])  # Output: [5, 4, 3, 2, 1]

#Duplicates in Lists

Afternoon = ["Trevor", "John", "Blessing", "Trevor", "Trevor", "Blessing"]
print(Afternoon)
#list Length
print(len(Afternoon))
#Type
print(type(Afternoon))

#acessing lists
print(Afternoon[2])
print(Afternoon[5])
print(Afternoon[-3])
#acessing range of items
print(Afternoon[3:6])
print(Afternoon[:5])
print(Afternoon[1:])
#Add List items
Afternoon.append("Martha")
print(Afternoon)
#Add list item using insert method
Afternoon.insert(0, "Livingstone")
print(Afternoon)
#Remove List items
Afternoon.remove("Livingstone")
print(Afternoon)
#Removing List items using index
Afternoon.pop(6)
print(Afternoon)