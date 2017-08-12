#!/usr/bin/python

import sys

try:
    f = open("test",'w')
    print >>f,"I love China"

except IOError,e:
    print e
