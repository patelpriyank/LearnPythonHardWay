from sys import argv
from os.path import exists

script, inputFileName = argv

def print_file(f):
    """documentation comments goes here"""
    print(f.read())

def print_line(f):
    """tell() gives you current pointer location in file"""
    print("@position %d: %r" %(f.tell(), f.readline()))

def rewind(f):
    """seek() moves pointer to given location in file"""
    f.seek(0)

def isExists(fileName):
    return exists(fileName)

print("Does input file exists? %r" % isExists(inputFileName))

if isExists(inputFileName):
    inputFile = open(inputFileName)
    print_file(inputFile)
    
    rewind(inputFile)
    print_line(inputFile)
    print_line(inputFile)
else:
    print("File not found")
