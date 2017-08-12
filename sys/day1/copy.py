#!/usr/bin/python

import sys

try:
    r = open(sys.argv[1],'r')
    w = open(sys.argv[2],'w')

    while True:
        buf = r.read(1024)

        if buf == '':
            break

        w.write(buf)
except:
    pass
