#http://effbot.org/zone/python-with-statement.htm

'''
A high-level explanation of the context management protocol is:

The expression is evaluated and should result in an object called a ``context manager''. The context manager must have __enter__() and __exit__() methods.
The context manager's __enter__() method is called. The value returned is assigned to VAR. If no 'as VAR' clause is present, the value is simply discarded.
The code in BLOCK is executed.
If BLOCK raises an exception, the __exit__(type, value, traceback) is called with the exception details, the same values returned by sys.exc_info(). The method's return value controls whether the exception is re-raised: any false value re-raises the exception, and True will result in suppressing it. You'll only rarely want to suppress the exception, because if you do the author of the code containing the 'with' statement will never realize anything went wrong.
If BLOCK didn't raise an exception, the __exit__() method is still called, but type, value, and traceback are all None.
'''

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

'''


with open("./App_Data/sample.txt") as f:
    data = f.read()
    print(data)

'''
2)
The threading module's locks and condition variables also support the 'with' statement:

lock = threading.Lock()
with lock:
    # Critical section of code
    ...
The lock is acquired before the block is executed and always released once the block is complete.
'''

from decimal import Decimal, Context, localcontext

#Displays with default precision of 28 digits
v = Decimal('578')
print("Default context: %r" %v.sqrt())

with localcontext(Context(prec=16)):
    print("Modified context: %r" %v.sqrt())

print("Back to Default context: %r" %v.sqrt())

'''
3)
Writing Context Managers
'''
class DatabaseConnection:
    def cursor(self):
        note = "Returns a cursor object and starts a new transaction"
        return note #self.cursor()
    def commit (self):
        note = "Commits current transaction"
        return note
    def rollback (self):
        note = "Rolls back current transaction"
        return note

    def __enter__(self):
        print("In __enter__()")
        note = "code to start new transaction"
        return note

    def __exit__(self, type, value, tb):
        print("In __exit__()")
        note = "code to do cleanup()"
        return note

with DatabaseConnection() as mydbconn:
    print(mydbconn)