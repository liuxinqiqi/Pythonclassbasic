#!/usr/bin/python

import sys

try:
    f = open(sys.argv[1],'r+')
    buf = f.read(10)
except IOError,e:
    print e

else:
    print buf
