#!/usr/bin/python

import os
from time import sleep
pid = os.fork()

if pid < 0:
    print "create process faile"
elif pid == 0:
    sleep(0.1)
    print "This is a child process:",os.getpid()
else:
    os.wait()
    print "This is parent process",os.getpid()
    while True:
        pass

print "++++++++++++++++++++++++"
