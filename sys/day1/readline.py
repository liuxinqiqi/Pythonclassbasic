#!/usr/bin/python

import sys

try:
    f = open(sys.argv[1],'r+')
#    buf = f.readline(5)
#    buf = f.readline()
except IOError,e:
    print e

#else:
#    print buf

while True:
    buf = f.readline()
    if buf == '':
        break
    print buf

