#Write a program to create a function that takes two arguments, name and age, and print their value.
def value( name, age):
    print(name,age)

value("Suma", 30)

#Create a function with variable length of arguments

print("--------Create a function with variable length of arguments [positional arbitary arguments]---------")
def add(*numbers):
    sum = 0
    print(sum)
    print(" 1st line")
    for i in numbers:
       print(i)
       sum = sum + i
       print ("total" + " " + str(sum))

add(10,25,10,10,10)

print("----------print multiple  arguments to a function using * Symbol-----")
def func(*args):
    for i in args:
      print(i)



func(10,20,3,4,2,5)

#Write a program to create function calculation() such that it can accept two variables and
# calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

print("--------- Addition & subtraction in single return call---------")

