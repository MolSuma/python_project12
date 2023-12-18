#Save the file in document:"rt" reead & write
print("------print upto specified characters-----")
f=open("D:\\Testing\\Demo_file1.txt", "rt")
print(f.read(17))
#read line--> read line by line
print("------read line-----")
f=open("D:\\Testing\\Demo_file1.txt", "rt")
print(f.readline())
print(f.readline())
f.close()
#for loop:-->for reading the file line by line
print("-------read all line using for loop----")
f=open("D:\\Testing\\Demo_file1.txt", "rt")
for x in f:
    print(x)
f.close()
#append--> writing to the exsisiting file: a--> append at the end: w--> over write the file
print("-------Adding new line-----")
f=open("D:\\Testing\\Demo_file1.txt", "a")
f.write(" New line is included")
f.close()
f=open("D:\\Testing\\Demo_file1.txt", "r")
print(f.read())
#write: keyword:  "w" Replace everything
print(" --------- write will replace all-------")
f=open("D:\\Testing\\Demo_file1.txt", "w")
f.write(" NewDelhi is the capital of india")
f.close()
f=open("D:\\Testing\\Demo_file1.txt", "r")
print(f.read())
# Createe a new file: keyword "x" new text file will be created
print("-------create a newfile: NAME: file5-------")
f=open("D:\\Testing\\Demo_file5.txt", "x")
print(" Deleting file4-----")
import os
os.remove("D:\\Testing\\Demo_file4.txt")
f.close()

