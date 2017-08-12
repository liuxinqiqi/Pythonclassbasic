#!/usr/bin/python

def func():
    print "hello kitty"


func()

a = func

print id(func)
print id(a)
print type(a)

a()
