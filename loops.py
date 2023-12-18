# While loop will execute as long as the ececution is true:
#increment
print("---------increment---------")
i=1
while i<10:
    print(i)
    i+=1  # i +=2 increment by 2

#Decrement
print("---------decrement---------")
i=10
while i>=1:
    print(i)
    i-=1
#break statement: will stop the execution of the loop even if the while statement is true
print("---------break---------")
i=1
while i<10:
    print(i)
    if i==5:
        break
    i+=1

# continue statement:  Stop the current situation and continue with rest of iteration:
print("---------continue---------")
i=1
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)
#else: combine else with while statement
print("---------else statement---------")
i=1
while i<6:
    print(i)
    i+=1
else:
    print(" is no longer less than 6")
#for loop: list of elements we can access using elemnts
print("---------for loop to access---------")
Name = ["sana", "Aarudh", "Ashi"]
for x in Name:
    print(x)

# break statemnt
print("---------for loop break statemnt---------")
Name = ["sana", "Aarudh", "Ashi", "Vinayak", "Vihana"]
for x in Name:
    print(x)
    if x=="Aarudh":
        break
#Continue: print sttmtat last
print("---------for loop in continue---------")
Name = ["sana", "Aarudh", "Ashi", "Vinayak", "Vihana"]
for x in Name:
    if x=="Aarudh":
        continue
    print(x)

#Range--> to repeat how many time, take only int value
print("---------for loop in rnage--------")
for x in range(6):
    print(x)
# range between values: similar like indexing
print("---------for loop in rnage between values--------")
for x in range(10,13):  # inbetween from 10 but less than 13
    print(x)
print("---------for loop in rnage between values and increment by 2--------")
for x in range(1,13, 2):  # inbetween from 1 but less than 13 & increment by 2
    print(x)
#pass : no validation and no error , no need to print anything use pass statement
print("---------for loop in pass stmt--------")
for x in range(6):
    pass


