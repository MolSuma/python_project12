# to define class fiest letter should be capital or Camel case: eg. MyClass, Not start with numners, no space
print("----------Declaration of object and class-----")
class Myclass:
    x=5

obj1 = Myclass() # Creating object for the class
print(obj1.x) # print the object declared in class or accesing

#Employee details:
print("--------Print employee details using class and objects declaration-------")
class EmployeeDetails:
    #  Declaration of Attributes
    Name="Arun"
    Employee_id="32142"
    Role="Test Engineer"
    Project="E-commerce"

# Accessing attributes
obj2 = EmployeeDetails()
print(obj2.Name)
print(obj2.Employee_id)
print(obj2.Role)
print(obj2.Project)
 # Declaring class & function
print("--------Print employee details using Methods declaration-------")
class EmployeeDetails:
    #  Declaring Attributes
    Name="Arun"
    Employee_id="32142"
    Role="Test Engineer"
    Project="E-commerce"
    #MEthods inside the class
    #Declaring function
    def func(self):
     print(EmployeeDetails.Name,"\n", EmployeeDetails.Employee_id,"\n",EmployeeDetails.Role ) # accessing attributes inside function

obj3 = EmployeeDetails()
obj3.func()
print(obj3.Project)

print("----------find the area of a rectangle using classes--------")
class Rectangle:
    length=int(input(" Enter the length of the rectangle:  "))
    breadth = int(input(" Enter the breadth of the rectangle:  "))




    def area(length, breadth):
        area1 = length * breadth
        print(Rectangle.area1)

        operation = Rectangle()
        operation.area(length,breadth)
        print(Rectangle.area1)



