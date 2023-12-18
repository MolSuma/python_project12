#Short hand if one conditon & one print statemetnt in one line
number1 =10
number2=10
if(number1==number2):print("Numbers are equal")
else:print("Numbers are not equal")

number1 =10
number2=5
if(number1>number2):print("Number1 greater than number2")
else:print("Number1 smaller than number2")

number1 =5
number2=10
if(number1<number2):print("Number1 smaller than number2")
else:print("Number1 smaller than number2l")

number1 =10
number2=10
if(number1>=number2):print("Number1 greater than or equal to number2")
else:print("Number1 is not greater than or equal to number2")


number1 =5
number2=10
if(number1<=number2):print("Number1 smaller than or equal to number2")
else:print("Number1 is not smaller than or equal to number2")

number1 =5
number2=10
if(number1!=number2):print("Numbers are not equal")
else:print("Numbers are equal")


#and conditions--> both conditions are true
a=10
b=31
c=43
if b>a and c>a:
    print("both conditions are true")
else:
    print("both conditions are false")

#or condition--> 1 condition is true
a=10
b=31
c=43
if a>b or c>a:
    print("any one  onditions is true")
else:
    print("both conditions are false")
#not condition
number1 =5
number2=10
if not (number1>number2):print("Number1 not grater than number2")

#nested if--> if statement inside another if statement

a= int(input("Enter the number:\n"))
if a>20:
    print("a greater than 20")
    if a>10:
        print("a greater than 10")
    else:
               print("but not above 20")





