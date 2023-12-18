# index: contineous memory data is stored - starts with 0
a = "hello world"
print(a[3])
print(a[5])
print(a[10])
print(len(a))

#check if- Gives true if it is present

text = "My name is Aarudh"
print("Aarudh" in text)

print ("Sana" in text)

#Check if not - Gives true if it is not present

text = "My name is Aarudh"
print("Aarudh" not in text)

print ("Sana" not in text)

# Slicing
a = "Hello world*"
print(a[2:11])

 #Slicing from start
a = "Hello world*"
print(a[:10])

#Slicing till start -till end
a = "Hello world*"
print(a[2:])
#Modifying
a = "Suma Mol"
print(a.lower())
print(a.upper())
print(a.strip())
print(a.replace("m","B"))

b = "Sana,Shree"
print(b.split(","))
print(b.split("n"))
print(b.split("h"))

# Concadination
a = "Sana"
b = "Shree"
c = a+b
print(c)
d = a+ " "+ b
print(d)

# Format
"""age=30
text = " My age is" + age
print(text)
"""


age= 30
text = "My age is {}"
print(text.format(age))

age1=21
age2=31
age3=10
text = "My age is {}, My mother age is {}, My son age is {}"
print(text.format(age1, age2, age3))

age1=21
age2=31
age3=10
text = "My son age is {2}, My mother age is {1}, My  age is {0}"
print(text.format(age1, age2, age3))

age1=21
age2=31
age3=10
text = "My son age is {2}, My mother age is {1}, My  age is {0}"
print(text.format(age3, age2, age1))

#backspace

