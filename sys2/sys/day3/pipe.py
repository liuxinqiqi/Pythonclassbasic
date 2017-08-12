#!/usr/bin/python 

import sys,os
from time import sleep

(r,w) = os.pipe()

pid = os.fork()

if pid < 0:
    print "fail to fork"
elif pid == 0:
    print "child:"
    os.close(w)
    r = os.fdopen(r)

    while True:
        buf = r.readline()
        print "buf : ",buf
        sys.stdout.flush()

    print "child close"
else:
    print "parent:"
    os.close(r)
    w = os.fdopen(w,'w')
    while True:
        buf = sys.stdin.readline()

        w.write(buf)
        w.flush()
