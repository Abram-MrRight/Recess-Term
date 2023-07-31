

#Day2
"""
Control Flow
-conditional statements: (if, elseif, else)

control flow is the order in which the program's code executes. 
The control flow of a Python program is regulated by 
-conditional statements
- loops
- function calls. 
This section covers the if statement and for and while loops; functions 

#if gen_gender_sex:
#    print("Male")
#else:
  #print('Female')

if condiction1:
   print('True')
elseif condition2:
  print("True")
else:
print("True")
"""

#Example 1

# age<18, "Your are underage"
# age>=18 and age <=65 "Your are an adult"
#print "You are a senior citizen"

#age = int(input())

# Exercise!:
age =50
if age <18:
  print("Your are underage")

elif age>=18 and age<=65:
  print("Your are an adult")
  
else:
  print("You are a senior citizen")


"""
#Loops
#Loops(for, while)
# for item in sequence

"""


#for loop
#Exercise2
fruits = ["orange", "Mango", "Banana", "Apple"]
for myFruits in fruits:
  print(myFruits)
  if myFruits == "Banana":
    break


#while loop
#Example3
x=0
while x <5:
  print(x)
  x+=1

#Exercise3
first_name = "Abraham"
lent2 = len(first_name)

while lent2 <10:
  print(" It matches the condition")
  print(lent2)
  lent2+=1
print("----------------------")


  #Break and continue statements
  #Break
for number in range(1, 10):
    if number ==5:
      break
    print(number)
print("-----------------------")




#Eercise4
fruits = ["orange", "Mango", "Banana", "Apple"]
for myFruits in fruits:
  print(myFruits)
  if myFruits == "Banana":
    continue


#Exception Handling(try, except, finally)
"""
try block:
except:
finally:
"""

try:
  x = 10/0
except ZeroDivisionError:
  print("You cant divide number by zero")
finally:
    print("This is always executed")




#Example5
#Dict is a dictionary {}

emotion = {
        'happy' :" I'm glad to hear you",
        'sad' : "I'm sorry to hear that your feeling sad.",
        'angry' : "take a deep breath and try to stay alive",
        'fearful' :"I understand that fear can be challenging",
        'disqusted' :"That's unfortunate to feel disqusted",
        }

#prompt the user to enter their emotions
user_emtion = input("How are you feeling today?")
if user_emtion in emotion:
  print(emotion[user_emtion])

print(user_emtion)





#EXERCISE: Write a program to ask students about their mental heath
# prompt students on a scale of 1-10 to raise their mental heath


print("Welcome to our Mental Health Survey!")
name = input("Enter your full name")

print(f"Hello, {name}! ")
print("-------------------------")

    # Ask survey questions
rating = int(input(" How would you rate your current mental health? (1 - Very poor, 10 - Excellent): "))
feeling = input("Have you been feeling stressed or overwhelmed lately? (Yes/No) ")
Disission = input("Do you have difficulty concentrating or making decisions? (Yes/No) ")
support = input("Are you actively seeking support or counseling for your mental health? (Yes/No) ")
exercise = input("Do you engage in regular physical exercise? (Yes/No): ")

    # Display survey results
print("\nOur survey results!")
print("-------------------------")
print(f"Student Name: {name}")
print("-------------------------")
print(f"Mental Health Rating: {rating}")
print("-------------------------")
print(f"Feeling Stressed or Overwhelmed: {feeling}")
print("-------------------------")
print(f"Difulity in concentration and making decisions: {Disission}")
print("-------------------------")
print(f"Seeking help: {support}")
print("-------------------------")
print(f"Engaging in Regular Physical Exercise: {exercise}")


 