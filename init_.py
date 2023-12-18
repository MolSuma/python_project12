#init()
'''class Car:
    def __int__(self):
        print(" I am the first func called in the class")


obj = Car()'''

#Add speed & limit
class Car:
    def __init__(self, model,speed):
        self.model=model
        self.speed=speed
        print(" I am the first func called in the class")


obj = Car( "Honda" , 120)
print(obj.model)
print(obj.speed)

#Personal details
class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age
        print(" I am the first func called in the class")
        print(" Name & age")


obj1 = Person( "Sana" , 8)
print(obj1.name)
print(obj1.age)
