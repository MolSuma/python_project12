#Dictionary
# ordered
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
print(thisdic)

# Duplicates not allowed in both key & value
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA",
"School" : "AIA"
}
print(thisdic)

#Changable
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA",
    "yyyy": "uytr",
"School" : "AIA"
}

#Access: one key value
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA",
"School" : "AIA"
}
print(thisdic["Name"])

#getmethod to get value of a particular key
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA",
"School" : "AIA"
}
print(thisdic.get("Name"))
# to get all keys in dictionary
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA",
"School" : "AIA"
}
x=thisdic.keys()
print(x)

# add new key& value in exsisting dic
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
x=thisdic.keys()
print(x) #before the change
thisdic["fav colr"] = "pink"
print(x) # after the change
print(thisdic)

thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
x=thisdic.keys()
print(x) #before the change
thisdic
print(x) # after the change
print(thisdic)


# to add multiple key and values update method
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
x=thisdic.keys()
print(x) #before the change
thisdic.update({'fav1':'red','fav2':'pink'})
print(x) # after the change
print(thisdic)