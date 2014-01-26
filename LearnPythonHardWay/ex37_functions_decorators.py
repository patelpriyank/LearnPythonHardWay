#! /usr/bin/env python
# -*- coding: utf-8 -*-

#functions are objects 
print(issubclass(int, object)) # all objects in Python inherit from a common baseclass

def foo():
    pass

print(issubclass(foo.__class__, object))

#you can pass functions to functions as arguments or return functions from functions as return values
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def apply(func,x,y):
    return func(x,y)

print(apply(add,10,40))
print(apply(sub, 40,-10))

'''
Returning functions as values
This may seem a little more bizarre. 
At point #1 I return the variable inner which happens to be a function label. 
There is no special syntax here - our function is returning the inner function which otherwise could not be called. 
Remember variable lifetime? The function inner is freshly redefined each time the function outer is called but if inner was not returned from the function it would simply cease to exist when it went out of scope.
'''

def outer():
    def inner():
        print("Inside inner")

    return inner

funcLabel = outer()
print(funcLabel)
print(funcLabel())

#************************************************ DECORATORS *************************************************************************

