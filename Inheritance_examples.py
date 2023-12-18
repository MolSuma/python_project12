#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
print("-------Write a Python program to create a Vehicle class with max_speed and mileage instance attributes---")
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        print(" I am the first function called in the class")
obj1=Vehicle(100,80)
print(obj1.max_speed)
print(obj1.mileage)

#Create a Vehicle class without any variables and methods
print("-----Create a Vehicle class without any variables and methods---")
class Vehicle:
    pass
#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
print("-----Create a child class Bus that will inherit all of the variables and methods of the Vehicle class----")
class Vehicle1:
    max_speed=""
    mileage=" "
    def func1(self):
        print("Parent class is initiating----")
class Bus(Vehicle1):
    def func2(self):
        print(" Child class is initiating---")
        print("Max_speed is", self.max_speed)
        print("Milage is", self.mileage)
obj2=Bus()
obj2.max_speed="100"
obj2.mileage="80"
obj2.func1()
obj2.func2()

#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

print("--- the capacity argument of Bus.seating_capacity() a default value of 50 --------")
class Vehicle2:
    max_speed = " "
    seating_capacity = " "
    def __init__(self):
        print(" Vehicle class initiating---")
class Bus2(Vehicle2):
    def func3(self):
        print(" Bus child class is initiating---")
        print("max_speed is", self.max_speed)
        print(" seating capacity is ", self.seating_capacity)

obj3=Bus2()
obj3.max_speed="200"
obj3.seating_capacity="50"
obj3.func3()





