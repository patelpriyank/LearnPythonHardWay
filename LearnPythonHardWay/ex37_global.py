#http://docs.python.org/2/library/traceback.html#traceback.format_exc
import sys, traceback


try:
    def local():
        me = "locally defined"
        print(me)

    local()
    print(me) ##error: me is not defined

except Exception as ex:
    print(ex)
    print(traceback.format_exc())

def globelevel():
    global her
    her = "she is just mine"
    print(her)

globelevel()

her = "now she is for everybody"
print(her)
    