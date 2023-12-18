#List Modification
#accessing list in specified range
list = [ "apple", "orange", "orange","banana", "orange"]
print(list)
print(list[1:4])
print(list[2:])
print(list[:2])
#Change single element
list = [ "apple", "orange", "orange","banana", "orange"]
list[2]= "Guava"
print(list)
# Change range of elements
list = [ "apple", "orange", "orange","banana", "orange"]
list[2:]= ["Guava" ,"kiwi", "papaya"]
print(list)
#insert elemnt using append()--> at the end of the list w

list = [ "apple", "orange", "orange","banana", "orange"]
list.append("xxxx")
print(list)
#insert()--> at specifird index
list.insert(1,"aaaaa")
print(list)
#Remove()___> to remove. if two items are there it will removee the first one
list = [ "apple", "orange", "orange","banana", "orange", "apple"]
list.remove("apple")
print(list)
#pop()--> to remove at specified index
list = [ "apple", "orange", "orange","banana", "orange", "apple"]
list.pop(3)
print(list)
#del--> to delete entire list, or at the specified indexz

list = [ "apple", "orange", "orange","banana", "orange", "apple"]
del list[0]
print(list)
#del--> to delete elements in specifeid range
list = [ "apple", "orange", "orange","banana", "orange", "apple"]
del list[0:4]
print(list)

list = [ "apple", "orange", "orange","banana", "orange", "apple"]
del list
print(list)

