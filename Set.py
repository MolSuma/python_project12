# Sets:
#unordered: each time if we print the sequence will change
myset= {"apple", "pomo", "kiwi", "banana", "orange"}
print(myset)

# # Not Allow duplicates--> apple 2 times
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
print(myset)

## Unchangable: cannot change the exsisting item. but can add or delete the items(can't modify exsisting data)
# via indexing we canit access the elelment
'''myset= {"apple", "pomo", "kiwi", "banana", "orange"}
myset[2] = "xxxx"
print(myset)'''

 #or loop
 # check if
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
print("pomo" in myset)

#Changing items: We cannot change the items once the set is created. You can add & remove the new item

#add item
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
myset.add("yyyyy")
print(myset)

#update method: To addd another set to the current set--> update to current set
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
newset={"aaaa","bbbbb","ccccc"}
myset.update(newset)
print(myset)

#remove method()--> to delete the particular item from set what we are giving
#remove will raise an error if the item to remove is not present but in discard we won't get error
#pop()--> randomly delete the item
#Union method--> to join the sets

myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
myset.remove("pomo")
print(myset)
'''
#raise an error
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
myset.remove("xxxx")
print(myset)'''
#wil delete the given item
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
myset.discard("pomo")
print(myset)
#discard--> no item will not produce error
myset= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
myset.discard("xxxx")
print(myset)
# Union will take new set---> will not update in exsisting set,
# we should take new set to store the data or update the data
myset1= {"apple", "pomo", "kiwi","apple", "banana", "orange"}
myset2={"xxxx", "yyyy"}
newset=myset1.union(myset2)
print(newset)

#pop()--> it will randomly delete any item in set
myset= {"apple", "pomo", "kiwi", "banana", "orange"}
myset.pop()
print(myset)