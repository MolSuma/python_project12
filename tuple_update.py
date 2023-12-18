#Tuple update--> convert tuple to list , update it and then covert back to tuple
#updating the exsisting tuple
tuple1= ("apple", "pomo", "kiwi", "banana", "orange")
list1= list(tuple1)
list1[1]="chikku"
newtuple=tuple(list1)
print(newtuple)


#Add items to tuple using append()
tuple1= ("apple", "pomo", "kiwi", "banana", "orange")
list1= list(tuple1)
list1.append("chikku")
newtuple=tuple(list1)
print(newtuple)

#remove the items in tuple
tuple1= ("apple", "pomo", "kiwi", "banana", "orange", "chikku")
list1= list(tuple1)
list1.remove("chikku")
newtuple=tuple(list1)
print(newtuple)
#unpacking-->assigning variable to each items
# allowing to extract the values into variables
tuple1= ("apple", "pomo", "kiwi", "banana", "orange", "chikku")
(a,b,c,d,e,f) = ("apple", "pomo", "kiwi", "banana", "orange", "chikku")
print(a)