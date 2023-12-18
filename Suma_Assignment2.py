# 1. String as input & print its length
string1 ="Sana Shree"
print(len(string1))

string2 = "My name is Sana Shree"
print(len(string2))

#2. prints number of words in a sentence #try with count
string2 = "My name is Sana Shree"
words = string2.split(" ")
print(words)
print(len(words))

#3.Convert a sentence into uppercase:
string2 = "My name is Sana Shree"
print(string2.upper())

#4.String as input & replace "a" as "e"
string = "aaaaaaaaaaaaaa"
print(string.replace("a", "e"))

#5.Check if two strings are similar:
#Equal strings
string1 = "My name is Sana Shree"
string2= "My name is Sana Shree"
print(string1.__eq__(string2))

# Unequal strings:
string1 = "My name is Sana Shree"
string2= "My name is Aarudh yuvan"
print(string1.__eq__(string2))

#6.  Check if a substring is present in a given string:

string1 = "My name is Sana Shree"
print ("name" in string1)
print ("Aarudh" in string1)

#7.Write a program to add item 7000 after 6000 in the following Python List # use index concept
list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]
for i in list1:
    print(i)
    if i==6000:
        find_index=list1.index(i)
        new_index=find_index+1
        list1.insert(new_index,7000)

    print(list1)



#8.Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
'''list1 = [5, 10, 15, 20, 25, 50, 20]
for i in list1:
    print(i)
    if i==20:
        find_index=list1.index(i)
        print(find_index)
        list1.pop(find_index)
        list1.insert(find_index,200)
        print(list1)
        break
'''
list1 = [5, 10, 15, 20, 25, 50, 20]
to_find=20
to_replace=200
for i in list1:
    print(i)
    if i==to_find:
        find_index=list1.index(i)
        list1.pop(find_index)
        list1.insert(find_index, to_replace)
        print(list1)
        break






