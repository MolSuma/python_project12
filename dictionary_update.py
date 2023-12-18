# Change the value of dicti:
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}

thisdic["Name"]= "Aarudh"
print(thisdic)
#both key values
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}

thisdic.update({'Name1':'Aarudh1'})
print(thisdic)
#Remove item from dic use pop()

thisdic["Name"]= "Aarudh"
print(thisdic)

thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}

thisdic.pop("Age")
print(thisdic)

#for loop
for x in thisdic:
    print(thisdic[x]) # since we have given pop it is deleting

#copying the dicitionary: copy(), dict()
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
print(thisdic)

#without coy()
mydic= thisdic
print(mydic)
#copy()
thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
print(thisdic)


mydic= thisdic.copy()
print(mydic)

thisdic = {
    "Name" : "Sana",
    "Age" : "7",
    "School" : "AIA"
}
