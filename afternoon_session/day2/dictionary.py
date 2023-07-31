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

