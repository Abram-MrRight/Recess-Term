
#comment
# single line comment




# multiple lines
"""
mutiline comments

"""







#Data structures(Data types)
"""
Numeric values are 1-10
integers = int
float =float (2.4, 3.14)

Strings = str
-single quote ('My name')
-double quote ("my age")

Boolean = (True, False)

sequence types
-list = enclosed with square brackets[]
-tuple =enclosed with parentheses{}
-range =iteration or loop

Mapping tpyes
-dict for dictionary enclosed with curly braces{}
{
name: 'Abram'
age: 23
}
or
{name: 'Abram', age:23}
item Dict
{apple, mango, banana}

Set Types
{apple, mango, banana} unordered collection types

None types
-represents null values

"""


#adta types
"""
A collection or grouping of data values ,
usually specified by a set of possible values
"""



# printing a simple text

print('Has been a nice lecture')

#variables
#student details
name ='Abram ' 
course= "Software Engineering"
age =60

# printing variables
print('My name is :'+name )
print('Im doing Bachelors in', course)
print('And im ',age, 'years old')



#Boolean
student_of_makerere= True
print(student_of_makerere)

#sequence type
string1 ='Im learning python'
print("\nstring with a single line quote")
print(string1)


# Creating a Dictionary
Dict = {1:'Messi', 2:'John', 3: 'Ronaldo'}
print("\nDictionary with the used of integers as key values")
print(Dict)



#using the len() with tuple 
phones = ("samsung", "iphone", "Techno", "samsung", "Techno")

length = len(phones)
print("The length of tuple is: ", length)
print('--------------------------------------')

# How to access tuples
phones = ("samsung", "iphone", "Techno", "samsung", "Techno")

#Accessing second item via index 
print(phones[1])
print('--------------------------------------')

#Negative indexing(last item in the tuple)
print(phones[-1])
print('--------------------------------------')

#Range of indexes

#Search starts at index 2 and ends at index 5
print(phones[2:5])
print('--------------------------------------')

#This returns items from beginning to, but leaves out forth item
print(phones[:4])
print('--------------------------------------')

#Range of Negative Indexes
#Returns the items from index -3 (included) to index -1 (excluded)
print(phones[-3:-1])
print('--------------------------------------')

#check if item exisits in a tuple
if 'iphone' in phones:
    print("Yes iphone is in the phones tuple")

print('--------------------------------------')




#finding the length of set, data types, accessing items in a set, Add items, Add two sets together
Cities = {"Kampala", "Nairobi", "Juba", "Cairo"}
bool_values = {True, False, False}

#Finding length
length =len(Cities)
print(length)
print('--------------------------------------')

#Data types
#All print<class, 'set'>
print(type(Cities))
print(type(bool_values))
print('--------------------------------------')



#Acessing items
#Looping through a set
for x in Cities:
    print(x)
print('--------------------------------------')

#Checking whether item exists
print("Nairobi" in Cities)
print('--------------------------------------')


#Add items in the set
Numbers ={10, 20, 40,30}

Numbers.add(70)
print(Numbers)
print('--------------------------------------')



#Adding two sets
Cities = {"Kampala", "Nairobi", "Juba", "Cairo"}
Countries = {"Uganda", "Kenya", "South Sudan", "Egypt"}

Cities.update(Countries)
print(Cities)
print('--------------------------------------')


# creating aList
Cities = ["Kampala", "Nairobi", "Juba", "Cairo"]
print(Cities)
#Data type
print(type(Cities))
print('--------------------------------------')

#List constructor
Cities = list(("Kampala", "Nairobi", "Juba", "Cairo"))
print(Cities)
