#1. Write a program to check whether a number is even or odd
#2. Write a program to accept number from 1 to 7 and display the name of the day like 1 for sunday , 2 for Monday and so on
#3.Write a program to check whether a person is senior citizen or not (age for SC -s 60)
#4.Write a program to find teh lowest nummer out of two numbers excepted from the user
#5.Write a program to convert a set into a tuple
#6. Write a program to remove the first given character from the first element of tuple

#1. Write a program to check whether a number is even or odd

print("------Even or odd-------")
number=int(input("Enter the number:  "))
if number%2==0: print( str(number) + "  is even")
else: print(str(number) + " is odd")

##2. Write a program to accept number from 1 to 7 and display the name of the day like 1 for sunday , 2 for Monday and so on

print("-------Days of week using ifelse stateement------")
number1=int(input("Enter the number"))
if number1==1: print(" First day of the week is Sunday")
if number1==2: print("Second day of the week is Monday")
if number1==3: print("Third day of the week is Tuesday")
if number1==4: print("Fourth day of the week is Wednesday")
if number1==5: print("Fifth day of the week is Thursday")
if number1==6: print("Sixth day of the week is Friday")
if number1==7: print("Seventh day of the week is Saturday")
else: print(" Invalid number")

print("--------Days of week using dictionary---------")
dict = {
      "1" : "Sunday",
     "2" : "Monday",
      "3" : "Tuesday",
       "4" : " Wednesday" ,
       "5" : "Thursday",
        "6"  : "Friday",
        "7"  : "Saturday"
}
number2= int(input (" Enter the number"))
print(dict.get(str(number2)))

#3.Write a program to check whether a person is senior citizen or not (age for SC -s 60)
print("-------Checking  whether a person is senior citizen or not-------")
age=int(input("Enter the age"))
if age>=60: print(" The person's age  is " + str(age)+ ": Senior citizen")
else : print(" The person is " + str(age)+ ": not senior citizen")


#4.Write a program to find teh lowest nummer out of two numbers excepted from the user
print("------Lowest of two numbers---------")
number3=int(input(" Enter the first number"))
number4=int(input(" Enter the second number"))
if(number3<number4): print(str(number3) + " is lowest number")
else: print(str(number4) + " is lowest number")

#5.Write a program to convert a set into a tuple
print("-----Convert set into tuple-------")
thisset = {"Sana","Aarudh", "Vihana", "Mahathi", "Vinayak"}
print(thisset)
print(type(thisset))
newset = tuple(thisset)
print(type(newset))
print(newset)

#6. Write a program to remove the first given character from the first element of tuple
print("------emove the first given character from the first element of tuple-----")

thistuple = ("Sana","Aarudh", "Vihana", "Mahathi", "Vinayak")
#print(thistuple)
#print(type(thistuple))
newlist= list(thistuple)
#print(newlist)
#print(type(newlist))
first_element=newlist[0]
#print(first_element)
#print(len(first_element))
new_element= first_element[1:]
#print(new_element)
newlist.remove(first_element)
newlist.insert(0, new_element)
#print(newlist)
newtuple = tuple(newlist)
print(thistuple)
print(newtuple)
