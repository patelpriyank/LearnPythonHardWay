'''
new slots, which weren't defined when the class was defined, can be created at will simply by assignment. 
Indeed, when working interactively, an empty class definition is often handy:
'''
#dynamic variables creation (slot)
class foo: pass
foo.a = 10
foo.b = 20

print(foo.a)
print(foo.b)

#Class Attributes vs Instance Attributes
class classInstance:
    a =  1

obj = classInstance()

print("Class value: %r" %classInstance.a)
print("Instance value: %r" %obj.a)

classInstance.a = "class level"
print("Class value: %r" %classInstance.a)
print("Instance value: %r" %obj.a)

obj.a = "instance level"
print("Class value: %r" %classInstance.a)
print("Instance value: %r" %obj.a)
print("Instance.__class__ value: %r" %obj.__class__.a)
