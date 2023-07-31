

#Excercise1: use the len() with this tuple example
phones = ("samsung", "iphone", "Techno", "samsung", "Techno")

length = len(phones)
print("The length of tuple is: ", length)
print('--------------------------------------')

#Exercise2: How to access tuples
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



#Exercise3: find the length of set, data types, accessing items in a set, Add items, Add two sets together
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