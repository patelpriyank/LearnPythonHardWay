#Command to execute> python Exercise15_ReadingFile.py ./App_Data/sample.txt
from sys import argv

script, filename = argv

print("We are going to erase %r" %filename)
print("If you don't want that press Ctrl + C")
print("If you are ok with that, press ENTER")
userSelection = input("?")

print("opening '%s' file for modification..." %filename)
fileData = open(filename, 'w')

#truncate file
print("Truncating '%s' file...." %filename)
fileData.truncate()

print("Let's write that file with your content. I am going to ask you to enter three lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#write file
print("Let's write these three lines to '%s' file" %filename)
fileData.write(line1)
fileData.write("\n")
fileData.write(line2)
fileData.write("\n")
fileData.write(line3)
fileData.write("\n")

print("and finally closing file...")
fileData.close()

#reading file line by line
print("Let's read this file line by line")

print("If you don't want that press Ctrl + C")
print("If you are ok with that, press ENTER")
userSelection = input("?")

print("Reopening '%s' file..." %filename)
fileData = open(filename)

# readline() vs readlines()

# readlines() : array of lines
lineCounter = 0
for line in fileData.readlines():
    print("Line %d: %s" %(lineCounter, line))
    lineCounter+=1

# readline() : one line, for loop loops throuhg each character of that particular line.
fileData = open(filename) #reopen file

charCounter = 0
for char in fileData.readline():
    print("Line %d: %s" %(charCounter, char))
    charCounter+=1

     