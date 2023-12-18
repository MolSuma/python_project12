#Assignment 5
#Create a python class with the below attributes and access the same via an object

#The class ‘Phone’ would have certain properties associated with such as:

#Color
#Cost &
#Battery Life
#Similarly, the class ‘Phone’ would have certain behavior associated with such as:

#You can make a call
#You can watch videos &
#You can play games
print("-------Class: phone access via objects------")
class Phone:
    color="Black" #Decleration of attributes
    cost="Rs.15,000"
    battery_life="10 hours"
obj=Phone()
print(obj.color)
print(obj.cost)
print(obj.battery_life)

print("-------Class: phone with certain behaviours------")
class Phone:
    color="Black" #Decleration of attributes
    cost="Rs.15,000"
    battery_life="10 hours"
    def make_a_call(self):
        print(" Making a phone call")

    def watch_videos(self):
        print(" Watching videos")

    def play_games(self):
        print(" Playing games")
obj1 = Phone()
obj1.make_a_call()
obj1.watch_videos()
obj1.play_games()



