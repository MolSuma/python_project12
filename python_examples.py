import cmath
import math
from random import random, randint


print("--------Square root of a number-------")
number=int(input("Enter the number: "))
print(" Square root of ",  str(number) + " is " ,math.sqrt(number))

print("-------Area of a Triangle------")
base=int(input("Enter the base of the triangle: "))
height=int(input("Enter the height of the triangle: "))
Area=0.5 * base * height
print(" The area of triangle with base ", str(base) + " and height ", str(height) + " is : ", str(Area))

print("------- Solve the quadratic equation------")
a=int(input(" Enter the value of  a:"))
b=int(input(" Enter the value of  b:"))
c=int(input(" Enter the value of  c:"))
#Discriminant value
d=b**2 - 4 * a * c
solution1= (-b + (cmath.sqrt(d)))/(2 * a)
solution2= (-b - (cmath.sqrt(d)))/(2 * a)
print("Solutions are ", str(solution1) + " and ", str(solution2))

print("-------program to swap two variables------")
number1=int(input("Enter the value of number1 :"))
number2=int(input(" Enter the value of number2: "))
temp_var=number1
number1=number2
number2=temp_var
print(" after swapping number1 is:" , str(number1))
print(" after swapping number2 is:" , str(number2))

print("------Generate a random number-----")
print(randint(1, 10))

print("------- kilometer to miles-----")
kilometer=int(input("Enter the value of kilometer: "))
miles=kilometer*0.621371
print(str(kilometer) + " kilometer is equal to ", str(miles) + " miles")

print("-------Celcius to farenhit-------")

