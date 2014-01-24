#http://effbot.org/zone/python-with-statement.htm

'''
def controlled_execution(callback):
        set things up
        try:
            callback(thing)
        finally:
            tear things down

    def my_function(thing):
        do something

    controlled_execution(my_function)

1)
with expression [as variable]:
    with-block

The expression is evaluated, and it should result in an object that supports the context management protocol. 
This object may return a value that can optionally be bound to the name variable. 
(Note carefully that variable is not assigned the result of expression.) 
The object can then run set-up code before with-block is executed and some clean-up code is executed after the block is done, 
even if the block raised an exception.

e.g.
with open('/etc/passwd', 'r') as f:
    for line in f:
        print line
        ... more processing code ...
2)
The threading module's locks and condition variables also support the 'with' statement:

lock = threading.Lock()
with lock:
    # Critical section of code
    ...
The lock is acquired before the block is executed and always released once the block is complete.
'''


with open("./App_Data/sample.txt") as f:
    data = f.read()
    print(data)
