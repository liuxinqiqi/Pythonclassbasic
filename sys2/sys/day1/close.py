#!/usr/bin/python

f = open('test','a')

print >>f,"hello world"

f.close()
#print >>f,"hello world"

with open('file','w') as f:
    print >>f,"hello world"
    print f.__doc__


#print >>f,"hello world"
