#Define method & attributes in parent class

print("----------Single inheritance--------")
class Animal:
    name=" "
    def eat(self):
        print(" I can eat")

class Dog(Animal):
    def display(self):
        print("My name is ", self.name)

beagle = Dog()
# data from parent class
beagle.name = " Elly"
beagle.eat()
#data from child class
beagle.display()

print("-----------Single inheritance------")

class App:
     app_name=" "
     app_version=" "
     app_device=" "

     def fetch_details(self):
         print(" fetching details---")

class AndriodApp(App):
    def tasks_of_app(self):
        print("App name is " , self.app_name)
        print(" App version is", self.app_version)
        print(" App device is", self.app_device)

obj = AndriodApp()
obj.app_name =" Whatsapp"
obj.app_version = " 2.0"
obj.app_device =" Android"
obj.fetch_details()
obj.tasks_of_app()

print("-----------Multiple inheritance--------")
class Father:
    father_name=" "
    Child_name=" "
    def ffunc1(self):
        print(" fetching father details-----")
class Mother:
    mother_name=" "
    child_name=" "
    def mfunc1(self):
        print(" fetching mother details")
class Childd(Father):
    def cffunc1(self):
        print(" father name is ", self.father_name)
        print( " child name is ", self.Child_name)
fobj1= Childd()
fobj1.father_name="Arun"
fobj1.Child_name = "Sana"
fobj1.ffunc1()
fobj1.cffunc1()

class Childd(Mother):
    def cmfunc2(self):
        print("Mother name is", self.mother_name )
        print(" Child name is ", self.child_name)
mobj1=Childd()
mobj1.mother_name=" Suma"
mobj1.child_name=" Sana"
mobj1.mfunc1()
mobj1.cmfunc2()






print("------- Multilevel inheritance------")


class App1:
    app_name = " "
    app_version = " "
    app_device = " "

    def fetch_details(self):
        print(" fetching details---")



class AndriodApp1(App1):
    def child1(self):
        print(" Child class 1 is executing----")


class AndroidApp2(AndriodApp1):
    def tasks_of_app(self):
        print("App name is ", self.app_name)
        print(" App version is", self.app_version)
        print(" App device is", self.app_device)


obj1 = AndroidApp2()
obj1.app_name = " Whatsapp"
obj1.app_version = " 2.0"
obj1.app_device = " Android"
obj1.fetch_details()
obj1.child1()
obj1.tasks_of_app()

print("-------Hirerchical inheritance------")
class Parent:
    name1=" "
    age1=" "
    def func1(self):
        print(" Fetching parent details----")

class eldr_child(Parent):
    def func2(self):
        print( " Fetching eldr_child details---- ")
        print( " Elder child name is ", self.name1)
        print(" Elder child age is ", self.age1)
obj2=eldr_child()
obj2.name1= " Sana"
obj2.age1= " 8"


class youngr_child(Parent):
    def func3(self):
        print(" Fetching youngr_Child details----")
        print(" Younger child name is ", self.name1)
        print(" Younger child age is ", self.age1)

obj3=youngr_child()
obj3.name1= " Aarudh"
obj3.age1="1.5"
obj2.func1()
obj2.func2()
obj3.func1()
obj3.func3()

print("---------Hybrid inheritance--------")
class Parent:
    name1=" "
    age1=" "
    def func1(self):
        print(" Fetching parent details----")

class eldr_child(Parent):
    def func2(self):
        print( " Fetching eldr_child details---- ")
        print( " Elder child name is ", self.name1)
        print(" Elder child age is ", self.age1)
obj2=eldr_child()
obj2.name1= " Sana"
obj2.age1= " 8"
obj2.func1()
obj2.func2()


class youngr_child(Parent):
    def func3(self):
        print(" Fetching youngr_Child details----")
        print(" Younger child name is ", self.name1)
        print(" Younger child age is ", self.age1)

obj3=youngr_child()
obj3.name1= " Aarudh"
obj3.age1="1.5"
obj3.func1()
obj3.func3()

class nephew(eldr_child):
    def func4(self):
        print(" Fetching nephew details for Elder child---")
obj4=nephew()
obj4.name1=" Mahathi"
obj4.age1="10"
obj4.func4()
obj4.func2()
obj4.func1()

class nephew(youngr_child):

    def func5(self):
        print(" Fetching nephew details of younger child----")
obj5 = nephew()
obj5.name1 = " Tharshith"
obj5.age1 = " 6"
obj5.func5()
obj5.func3()
obj5.func1()








