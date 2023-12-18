#Tuple--> not possible to add, modify, insert: We can join, loop, update, unpack, access
#ordered--> print same way
tuple= ("apple", "pomo", "kiwi", "banana", "orange")
print(tuple)

# Allow duplicates--> apple 2 times
tuple= ("apple", "pomo", "kiwi","apple", "banana", "orange")
print(tuple)

#length function --> to find length of tuples
tuple= ("apple", "pomo", "kiwi", "banana", "orange")
print(len(tuple))

#Type--> return the datatype as tuple
tuple= ("apple", "pomo", "kiwi", "banana", "orange")
print(type(tuple))

#Accessing tuples--> using index value
tuple= ("apple", "pomo", "kiwi", "banana", "orange")
print(tuple[1])
print(tuple[1:3])
print(tuple[1:])
print(tuple[:2])

#Looping
tuple= ("apple", "pomo", "kiwi", "banana", "orange")
for i in range(len(tuple)):
    print(tuple[i])

#join
tuple1= ("apple", "pomo", "kiwi","xxxxx")
tuple2= ( "banana", "orange")
tuple= tuple1 + tuple2
print(tuple)
#immutable: we cannot change the values directly for that we need to convert tuple into list
