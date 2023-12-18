#Encapsulation:
class Employee:
    def __init__(self, name, salary):
#private data members: keyword: single underscore:_
                self._name= name
                self._salary= salary
#public Methods to access the above private data
    def show(self):
        print("Name:" , self._name)
        print(" Salary: ", self._salary)
# create objext for class
emp=Employee("Ravi", "1000")
emp.show()




