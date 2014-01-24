#Command to execute> python Exercise15_ReadingFile.py ./App_Data/sample.txt

from sys import argv

script, filename = argv

print("You are executing script: %s" %script)
print("Here is your file name: %s" %filename)

fileData = open(filename)
print("""File content as below
%s
""" %fileData.read())

fileData.close()

filename = input("Type the file name again: \n>")
fileData = open(filename)
print(fileData.read())

fileData.close()