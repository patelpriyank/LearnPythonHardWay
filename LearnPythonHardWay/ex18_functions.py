def print_any(*args):
    for arg in args:
        print("%s" %arg)

def print_two(arg1, arg2):
    print("%r %r" %(arg1, arg2))

def print_none():
    print("i got nothing")

print_any(1,2,3,4,5)

arg1 = 'one'
arg2 = 'two'
print_two(arg1, arg2)
print_none()
    