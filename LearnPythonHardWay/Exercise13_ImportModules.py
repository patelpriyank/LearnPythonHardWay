from sys import argv

script, first, second, third = argv

print("%s %s %s %s" %(script, first, second, third))

print("your script is called %r" %script)
print("first variable: %r" %first)
print("second variable: %r" %second)
print("third variable: %r" %third)

userinput = input("enter fourth variable: ")
print("user entered variable is %r" %userinput)

