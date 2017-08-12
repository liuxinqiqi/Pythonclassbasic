#!/usr/bin/python
#coding=utf-8

def fun(a,b = 100,*c):
    print a
    print b
    print c


fun(1,2,3,4,5)
print "============================"
def fun1(a,b = 100,*c,**d):
    print a
    print b
    print c
    print d

fun1(1,2,3,4,5,c = 6,d = 7)
