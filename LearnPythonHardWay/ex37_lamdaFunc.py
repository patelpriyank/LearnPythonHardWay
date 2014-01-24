#Ref: http://www.secnetix.de/~olli/Python/lambda_functions.hawk

def f(x):
    return lambda x: x**2

def incrementby(n):
    return lambda x: x + n

a = incrementby(10)
b = incrementby(20)

print("%d, %d" %(a(0),b(0)))

print("%d, %d" %(a(5), b(5)))

print("%d" %incrementby(750)(150))

##-----------------
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(None, foo)) #returns <filter object at 0x00000000033481D0>

#http://stackoverflow.com/questions/10938066/python-interpreter-returns-objects-functions-instead-of-evaluating
print(list(filter(None, foo)))

print("Multiples of 3:\n%r" %list(filter(lambda x: x % 3 == 0 , foo)))

#************ Find prime numbers from the list ************
numbers = range(1, 100)
# all numbers that are multiples of divisors (2,3,5 & 7) cannot be prime numbers
divisors = [2,3,5,7]

for divisor in divisors:
    numbers = list(filter(lambda x: (x == divisor or x % divisor != 0),numbers))

print(list(numbers))


#************ split the sentence ************
sentence = 'It is raining cats and dogs'
words = sentence.split()
print(words)
print(list(map(lambda word: len(word), words))) #map(): Apply function to every item of iterable and return a list of the results. 

