print("--------try & multiple except------")
x=5
try:
    print(x)
except NameError:
    print(" Variable x is not defined")
except:
    print("something went wrong")
'''
#else --> used to define a block of code to be ececuted if no errors where raised
print("--------else--------")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print(" Nothing went wrong")

#finally
print("--------finally-----")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print(" Nothing went wrong")
finally:
    print("close the browser")

#custom exceptions: define exceptions based on the requirement  using raise keyword  if the condition occurs
print("------custom exceptions with no error-------")
x=1
print("No error")
if x<0:
    raise Exception("Sorry no numbers below zero are allowed")
print("------custom exceptions with error(we have given the condition)-------")
x=-1
if x<0:
    raise Exception("Sorry no numbers below zero are allowed")'''
