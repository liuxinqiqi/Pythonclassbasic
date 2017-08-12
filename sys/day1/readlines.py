#!/usr/bin/python

import sys

try:
    f = open(sys.argv[1],'r+')
    buf = f.readlines(3)
except IOError,e:
    print e

else:
    print buf
