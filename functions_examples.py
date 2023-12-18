# function :  one function can be used in number of times
#define it:
print()
def func():
    print("This is my first function")

#to call function
def func():
    print("This is my first function")

func()

#Divison of numbers using function:
'''def div():
    number1=int(input("Enter the number"))
    number2 = int(input("Enter the number"))
    Divide=number1/number2
    print(Divide)
    

div()

#Passing argumnets in func
def div(a,b):  #passing parameters
    c=a/b
    print(c)

div(10,2)  # calling func
div(6,3)
div(23, 6)'''

def add(a,b):
    c=a+b
    print(c)

add(10,3)
add(2.3, 4)
add(0, 21)

#lambda function: It can take any number of arguments but only one expression(add or sub)
# only one logic
print("--------lambda-------")
x= lambda a: a+ 10
print(x(5))

x= lambda a,b: a*b # define & expression in one line
print(x(10,2))