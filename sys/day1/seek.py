#!/usr/bin/python

f = open('new','w+')

f.write('hello world')

f.flush()

print f.tell()

f.seek(-5,2)

str = f.read()

print ">>>>",str
