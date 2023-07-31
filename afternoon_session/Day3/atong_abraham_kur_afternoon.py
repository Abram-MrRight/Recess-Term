

# EXERCISE1 (Lists)

print("EXERCISE 1: LISTS")
# Num1 Create a list with 5 items (names of people) and write a python program to output the 2nd item
names = ['Mun', 'Yak', 'Ghai', 'Atong', 'Mabiei']  

# Output the second element
second_element = names[1]
print(second_element)
print("--------------------------------------")

# Num2 Write a python program to change the value of the first item to a new value
names = ['Mun', 'Yak', 'Ghai', 'Atong', 'Mabiei']  

# Change the value of the first item
new_value = 'Daniel'
names[0] = new_value

# Print the updated list
print(names)
print("--------------------------------------")

# Num3 Write a python program to add a sixth item to the list
names = ['Mun', 'Yak', 'Ghai', 'Atong', 'Mabiei']  

# Add a sixth item to the list
new_item = 'Deng'
names.append(new_item)

# Print the updated list
print(names)
print("--------------------------------------")


#Num4 Write a python program to add “Bathel” as the 3rd item in your list
names = ['Mun', 'Yak', 'Ghai', 'Atong', 'Mabiei']  

# Add "Bathel" as the 3rd item in the list
new_item = 'Bathel'
names.insert(2, new_item)

# Print the updated list
print(names)
print("--------------------------------------")

# Num6 . Use negative indexing to print the last item in your list
my_list = [50, 20, 10, 80, 30]

# Print the last item using negative indexing
last_element = my_list[-1]
print(last_element)  
print("--------------------------------------")


# Num 7: Create a new list with 7 items and print the 3rd, 4th, and 5th items using a range of indexes
new_list = ['oxygen', 'nitrogen', 'nickel', 'zinc', 'sodium', 'calcium', 'barium']
items345 = new_list[2:5]
print("Items 3, 4, 5:", items345)
print("--------------------------------------")

# Num 8: Write a list of countries and make a copy of it
countries = ['Uganda', 'Kenya', 'Rwanda', 'South Sudan', 'Brundi']
countries_copy = countries.copy()
print("Countries Copy:", countries_copy)
print("--------------------------------------")

# Num 9: Loop through the list of countries
print("Countries:")
for country in countries:
    print(country)
print("--------------------------------------")

# Num 10: Write a list of animal names and sort them in both descending and ascending order
animal = ['elephant', 'lion', 'giraffe', 'tiger', 'zebra']
sortedAsc = sorted(animal)
sortedDec = sorted(animal, reverse=True)
print("Ascending Order:", sortedAsc)
print("Descending Order:", sortedDec)
print("--------------------------------------")

# Num 11: Output only animal names with the letter 'a' in them
animal_list = ["dog", "cat", "elephant", "lion", "tiger", "panda", "giraffe"]

animals_with_a = [animal for animal in animal_list if 'a' in animal]

print("Animal names with 'a':", animals_with_a)
print("--------------------------------------")


# Num 12: Write two lists of first and second names, then join them
first_names = ['John', 'Abraham', 'Kelvin']
second_names = ['Derick', 'Turabu', 'Emma']
full_names = first_names + second_names
print("Full Names:", full_names)
print("--------------------------------------")






# Exercise2 (Tuples)
print("EXERCISE 1: TUPLES---------")

# Num 1: Output your favorite phone brand
favorite_phones = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = favorite_phones[1]
print("Favorite Phone Brand:", favorite_brand)
print("--------------------------------------")

# Num 2: Print the 2nd last item in the tuple using negative indexing
second_last_element = favorite_phones[-2]
print("Second Last Item:", second_last_element)
print("--------------------------------------")

# Num 3: Update "iphone" to "itel"
favorite_phones = list(favorite_phones)
favorite_phones[favorite_phones.index("iphone")] = "itel"
favorite_phones = tuple(favorite_phones)
print("Updated Tuple:", favorite_phones)
print("--------------------------------------")

# Num 4: Add "Huawei" to the tuple
favorite_phones = favorite_phones + ("Huawei",)
print("My updated Tuple:", favorite_phones)
print("--------------------------------------")

# Num 5: Loop through the tuple
print("Looping Through Tuple:")
for item in favorite_phones:
    print(item)
print("--------------------------------------")

# Num 6: Remove the first item in the tuple
favorite_phones= favorite_phones[1:]
print("Updated Tuple:", favorite_phones)

# Exercise 7: Create a tuple of cities in Uganda using tuple() constructor
uganda_cities = tuple([ "Jinja", "Entebbe","Kampala", "Gulu"])
print("Uganda Cities Tuple:", uganda_cities)
print("--------------------------------------")

# Num 8: Unpack the tuple
# unpacking python tuple using *
# first and last will be assigned to x and z
# remaining will be assigned to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)
 
# print details
print(x)
print(y)
print(z)
print("--------------------------------------")


# Num 9: Print the 2nd, 3rd, and 4th cities in the tuple
print(uganda_cities[1:4])
print("--------------------------------------")

# Num 10: Join two tuples of first and second names
firstNames = ("Solomon", "Aguero", "Dbrayne")
secondNames = ("Ederson", "Alvares", "Foden")
fullNames = firstNames + secondNames
print("Full Names:", fullNames)
print("--------------------------------------")

# Num 11: Multiply a tuple of colors by 3
colors = ("yellow", "blue", "black")
multiplied = colors * 3
print("Multiplied Colors:", multiplied)
print("--------------------------------------")

# Num 12: Count the number of times 8 appears in the tuple
my_tuple = (10, 20, 7, 8, 9, 5, 3, 7, 8, 11)
countEights = my_tuple.count(8)
print("Number of 8s:", countEights)
print("--------------------------------------")





# Exercise3 (Sets)
print("EXERCISE 1: SETS---------")

# Num 1: Create a set of 3 favorite beverages using the set() constructor
my_beverages = set(["juice", "tea", "coffee"])
print("Favorite Beverages Set:", my_beverages)
print("--------------------------------------")

# Num 2: Add 2 more items to the beverages set
my_beverages.update(["water", "milk"])
print("My Updated beverages Set is:", my_beverages)
print("--------------------------------------")


# Num 3: Check if "microwave" is present in the set
my_set = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in my_set:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# Num 4: Remove "kettle" from the set
my_set.remove("kettle")
print("Updated Set:", my_set)
print("--------------------------------------")

# Num 5: Loop through the set
print("Looping Through Set:")
for item in my_set:
    print(item)
    print("--------------------------------------")


# Num 6: Add elements from a list to a set
my_set = {8, 9, 10, 11}
my_list = ["apple", "banana"]
my_set.update(my_list)
print("Updated Set:", my_set)
print("--------------------------------------")

# Num 7: Join sets of ages and first names
ages = {25, 30, 35}
first_names = {"John", "Alice", "Michael"}
joined_set = ages.union(first_names)
print("Joined Set:", joined_set)
print("--------------------------------------")





#Exercise 4 (Strings)
print("EXERCISE 1: Strings---------")

# Num 1: Concatenate an integer and a string
number = 25
fruit= "apples"
concat = str(number) + fruit
print("Concatenated String is:", concat)
print("--------------------------------------")

# Num 2: Output the string without spaces at the beginning, in the middle, and at the end
my_text = " Hello, world! "
stripped = my_text.strip()
print("After stripping the string:", stripped)
print("--------------------------------------")

# Num 3: Convert the value of 'my_text' to uppercase
upper = my_text.upper()
print("Uppercase String is :", upper)
print("--------------------------------------")

# Num 4: Replace 'U' with 'V' in the string
replaced = my_text.replace('U', 'V')
print("Replaced String:", replaced)
print("--------------------------------------")

# Num 5: Return a range of characters in the 2nd, 3rd, and 4th position
txt = "Lecture was amazing"
my_range = txt[1:5]
print("Range of Characters is:", my_range)
print("--------------------------------------")

# Num 6: Correct the error in the string
x = 'Hello! "welcome back" home!'
corrected = 'Hello! \"welcome back\" home!'
print("After being corrected :", corrected)
print("--------------------------------------")





 
#Exercise5 (Dictionaries)
print("EXERCISE 1: Dictionaries---------")

# Num 1: Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print("The size of the shoe is:", shoe_size)
print("--------------------------------------")

# Num 2: Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Updated Dictionary:", Shoes)
print("--------------------------------------")

# Num 3: Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("My updated one is:", Shoes)
print("--------------------------------------")

# Num 4: Return a list of all the keys in the dictionary
my_keys = list(Shoes.keys())
print("---Keys List is ---", my_keys)
print("--------------------------------------")

# Num 5: Return a list of all the values in the dictionary
values = list(Shoes.values())
print("---Values List------", values)

# Num 6: Check if the key "size" exists in the dictionary
if "size" in Shoes:
    print("--Key size exits")
else:
    print("Key size does not exit")

# Num 7: Loop through the dictionary
print("-----Looping Through Dictionary-------")
for key, value in Shoes.items():
    print(key, ":", value)

# Num 8: Remove "color" from the dictionary
del Shoes["color"]
print("After deleting, dictionary is :", Shoes)
print("------------------------")


# Num 9: Empty the dictionary
Shoes.clear()
print("After clearing all items in the dictionary ", Shoes)
print("------------------------")

# Num 10: Make a copy of a dictionary
first_dict = {"fruit": "mango", "color": "red"}
copied_dict = first_dict.copy()
print("Copied dictionary is :", copied_dict)
print("------------------------")

# Num 11: Nested dictionaries
inner_dict = {
    "lecturer1": {
        "name": "Jeff",
        "title": "doctor"
    },
    "lecturer2": {
        "name": "Livingstone",
        "title": "professor"
    }
}
print("inner Dictionary:", inner_dict)