from sys import argv
from os.path import exists

script, fromFileName, toFileName = argv

print("Copying file from %s to %s" %(fromFileName, toFileName))

from_fileData = open(fromFileName).read()

print("Input file is %d byels long" % len(from_fileData))

#output file
print("Does the output file exist? %r" % exists(toFileName))

print("Ready to copy file? hit RETURN to continue, CTRL-C to abort.")
input(">")

to_file = open(toFileName, 'w')
to_file.write(from_fileData)

print("Copy is completed!!")

to_file.close()