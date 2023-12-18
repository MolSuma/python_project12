# Polymorphism function over loading
# different class with same method
class operations:
    def __init__(self):
        print(" First function initiating----")
class Arithmetic_operations:
     def add(self, a,b):
        c = a + b
        print(" Addition of two number is---", str(c))
obj1=Arithmetic_operations()
obj1.add(2,3)
class Arithmetic_operations1:
    def add(self,a,b,d):
        c=a+b+d
        print(" Addition of two number is---", str(c))
obj2=Arithmetic_operations1()
obj2.add(3,4,5)





