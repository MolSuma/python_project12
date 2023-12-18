#Assignment 4 :
# 1. Print First 10 natural numbers using while loop
#2. Calculate the sum of all numbers from 1 to a given number
#3.Write a program to print multiplication table of a given number - 2
#4.write a program to print first 10 odd numbers
#5.Write a program to find the factorial of a number


print("--------- 1. Print First 10 natural numbers using while loop--------")
i=1
print(" First 10 natural numbers are:")
while i<=10 :
    print(i)
    i+=1

print("------2.Calculate the sum of all numbers from 1 to a given number-------")
i=1
a=int(input(" Enter the number: "))
sum=0
while i<=a:
    print(" The value of 'i' is " + str(i))
    sum= sum + i
    print("Sum of first " + str(i) + " natural numbers are: " + str(sum))
    i+=1

print("----------#3.Write a program to print multiplication table of a given number - 2------------")

#1*2=2, 2*2=4


a=int(input("Enter the number to get the table: "))
print("Table of " +str(a))
i=1
for i in range(11):
    b= a * i
    print(str(a)+ " * " + str(i) + " = " + str(b))


print("----------#4.write a program to print first 10 odd numbers--------")
#1,3,5,7.....19
#a%2!=0
def odd(a):
 b= a/2
 print(" The first " +str(b)+ " odd numbers are:" )
 for i in range(a):
     if i%2!=0:
      print(i)
     else:
         pass

odd(20)

#5! = 5*4*3*2*1
import math
print("---------#5.Write a program to find the factorial of a number---------")
a=int(input("Enter the number: "))
print("Factorial of " + str(a) + " is " + str(math.factorial(a)))




