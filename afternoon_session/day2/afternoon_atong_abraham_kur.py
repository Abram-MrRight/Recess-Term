

#exercise1: use the values() method to return a list of all values in the dictionary
mydict = {
    "phone" : "iphone",
    "iphoneModel" : "iphone15",
    "year" : [2023, 2022, 2021],
    "colors": ["red", "white", "blue"]
}
print("TList of values in a dictionary")
print(list(mydict.values()))


#Exercise2: to check if a key does exit in your dictionary
mydict = {
    "phone" : "iphone",
    "iphoneModel" : "iphone15",
    "year" : [2023, 2022, 2021],
    "colors": ["red", "white", "blue"]
}
if "year" in mydict:
    print("Exists")
else:
    print("Does not exist")




#Exercise 3: Give an example on how to change dictionary items, How to update
dict_2 = {
    "a": 1,
    "b":2, 
    "c":3   
}

# Adding a new item with an existing key (overwriting the value)
dict_2['b'] = 6

print(dict_2)


#Updating item with update() function
internal_marks = {'a':8}
dict_2.update(internal_marks)
print("New updated dictionary--------")
print(dict_2)



#Exercise 4: Give an example on how to add dictionary items, How to remove dictionary items
# Adding a new item
dict_2['d'] = 5
print("After adding an item in a dictionary--------")
print(dict_2)

# Removing an item using the del keyword
del dict_2['b']
print("After deleting an item--------")
print(dict_2)

# Removing and retrieving the value of an item using pop()
removed_value = dict_2.pop('c')
print(removed_value)
print("Removed value:", removed_value)




#Exercise 5: Give an on how you can loop through a dictionary and also how to nest a dictionaries

# Loop through the dictionary
for key, value in dict_2.items():
    print(key, value)

#Nesting in dictionary
lecturer = {'name': 'John', 'age': 20}
student = {'name': 'Jane', 'age': 19}

my_nesting = {'lecturerer': lecturer, 'student': student}

# Accessing nested dictionary values
print(my_nesting['lecturer']['name']) 
print(my_nesting['student']['age']) 



#Exercise One: Use a condition to show how to use boleans
# Example scenario: Checking if a student's score is above the passing threshold

Normal_temperature = 37
Not_normal = 50

# Checking the temperature condiction of a patien
if Not_normal >= Normal_temperature:
    print("You are in a bad condiction")
else:
    print("Everthing is normal")





#Exercise1 use the len() function to determine the length of the string
myString = "What a nice day!"
length =len(myString)
print(length)


#ExercieTwo:  Give an example of using a for loop in a string
my_name= "Atong Abraham"

# Loop through each character in the string
for character in my_name:
    print(character)


#Exercise Three: Give an example of slicing in strings
# Slicing the string
my_name= "Abraham"

slice1 = my_name[0:5]  # Slice from index 0 to 4 (exclusive)
slice2 = my_name[7:]   # Slice from index 7 to the end
slice3 = my_name[:5]   # Slice from the start to index 4 (exclusive)
slice4 = my_name[::2]  # Slice with a step size of 2

# Printing the slices
print(slice1) 
print(slice2)  
print(slice3) 
print(slice4)  


# APPLICATION OF THE CONCEPT





# NOTES--------

"""
# DICTIONARIES-----------------------------------------
#Dictionaries are used to store data values in key:value pairs.
#Dictionaries are ordered, changeable but do not allow duplicates
#Dicts can have items of any data type

mydict = {
    "phone" : "iphone",
    "iphoneModel" : "iphone15",
    "year" : [2023, 2022, 2021],
    "colors": ["red", "white", "blue"]
}
print(mydict)

#length of dictionary
print(len(mydict))

#Data type
print(type(mydict))
#Access Dictionary items
z = mydict["year"]
print(z)
y =mydict.get("iphoneModel")
print(y)
w = mydict.keys()
print(w)

#Dict constructor
myCont = dict( name ="Iphone", madeIn ="Ug", year= "2023")
print(myCont)

#exercise1: use the values() method to return a list of all values in the dictionary
#Exercise2: to check if a key does exit in your dictionary
#Exercise Three: Give an example on how to change dictionary items, How to update
#Exercise Four: Give an example on how to add dictionary items, How to remove dictionary items
#Exercise Five: Give an on how you can loop through a dictionary and also how to nest a dictionaries


#STRINGS-------------------------------------------------------------------
print("Afternoon")
print('Afternoon')

#Assign string to a variable
w = "Evening"
print(w)
#Multiline strings


#String as arrays
a = "Afternoon"
print(a[1])

#Exercise1 use the len() function to determine the length of the string
#Exercie Two Give an example of using a for loop in a string
#Exercise Three: Give an example of slicing in strings

# How to modify strings 
a = "Afternoon"
print(a.lower())
print(a.upper())

# Removing white space
b = " Afternoon "
print(b.strip())

#string concatenation
c = "Afternoon"
d = "Class"
w = c + d
print(w)
z = c + " " + d
print(z)

#NUMBERS--------------------------------
# integers, floats, complex
w= 10 # int
r= 3.9 #float
s = 2j #complex

print(type(w))
print(type(r))
print(type(s))

#Integers

a =2
b =3456789
c = -4567

print(type(a))
print(type(b))
print(type(c))

#Floats

g =2.89
z =3.3
e =-76.903

print(type(g))
print(type(z))
print(type(e))

#Complex Numbers
w =6 + 10
t =4j
h =-2j

print(type(w))
print(type(t))
print(type(h))

#Convert from int to complex

z = complex(w)
print(z)
print(type(z))

#Convert from int to float
#Convert from float to complex
#Convert from float to complext


#Convert from int to float:
first_number = 20
value = float(first_number)
print(value) 


#Convert from float to complex
second_number = 10.02
my_complex = complex(second_number)
print(my_complex) 

#Convert from float to complex with a complex part:
third_number = 9.6
my_value = complex(third_number, 1.8)
print(my_value)  



# BOOLEAN--------------------------------------------

#Works mostly when you wantto specify a variable type

h = int(20) #h is 20
y = int(30000) #y is 30000
a = int("8") #a is 8

print(h)
print(y)
print(a)
print(type(a))

#FORMAT-----------------------------
# Work when one wants to combine a string to number
#We need to use format() method
# The format () takes the passed parameters, format them and places
# Them in the string where the placeholder {}are

age = 23
name = "My name is Abraham, Im  {}" 
print(name.format(age))



"""