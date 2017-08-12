#!/usr/bin/python

a,b = 1,2

if a < b:
    print "a < b"
else:
    print "a >= b"


if a > b:
    print "a > b"
elif a == b:
    print "a = b"
else:
    print "a < b"

if a > b:
    if a > 0:
        pass
    else:
