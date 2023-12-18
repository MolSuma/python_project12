# Check if the items present
list = [ "apple", "pomo", "kiwi","banana", "orange"]
if "apple" in list:
    print(" Item present")
else:
    print("Not present")
#Item not present
list = ["apple", "pomo", "kiwi", "banana", "orange"]
if "toy" in list:
        print(" Item present")
else:
        print("Not present")

 #Check if not present(Item there)

list = ["apple", "pomo", "kiwi", "banana", "orange"]
if "apple" not in list:
    print(" Yes Item not present")
else:
    print("No item  present")
 # check if not present(Item not there)
list = ["apple", "pomo", "kiwi", "banana", "orange"]
if "toy" not in list:
    print(" Yes Item not present")
else:
    print("No item  present")

#Multiple if statement
list = ["apple", "pomo", "kiwi", "banana", "orange"]
if "apple"  in list:
    print(" Yes Item  present")
if "toy" in list:
    print("Yes item present")
else:
    print("No item  present")

#for loop for accessing the list items: here i represent elements in the list
list = ["apple", "pomo", "kiwi", "banana", "orange"]
for i in list:
    print(i)

#range() & method() --> range represent index
list = ["apple", "pomo", "kiwi", "banana", "orange"]
for i in range(len(list)):
    print(list[i])

#Sorting: Always in alpha numeric & ascending in default: sort()
#Sorting alphabets in A->Z
list = ["apple", "pomo", "kiwi", "banana", "orange"]
list.sort()
print(list)
#sorting alphabets Z->A
list = ["apple", "pomo", "kiwi", "banana", "orange"]
list.sort(reverse=True)
print(list)
#sorting numbers in ascending order
list = [2, 4,1,3,6,2]
list.sort()
print(list)
#sorting numbers in descending order
list = [2, 4,1,3,6,2]
list.sort(reverse=True)
print(list)

#Join()--> to join two list using + operator
list1 = ["apple", "pomo", "kiwi","xxxx"]
list2 =list = [ "banana", "orange"]
list3 = list1 + list2
print(list3)
list3.sort()
print(list3)

#copy--> to copy the list
list = ["apple", "pomo", "kiwi", "banana", "orange"]
copylist=list.copy()
print(copylist)