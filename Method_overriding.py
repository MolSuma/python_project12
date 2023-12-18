#concept inheritance is used in overriding
class Vehicle:
    def __init__(self, brand, model):
        self.brand= brand
        self.model=model

    def move(self):
            print(" Moving")
class Boat(Vehicle):
    def move(self):
        print("sail")
b= Boat("izbia", " Model 10")
print(b.brand,b.model)
b.move()
class Plane(Vehicle):
    def move(self):
        print("flying")
p=Plane(" Being", " Model 6")
print(p.brand, p.model)
p.move()
