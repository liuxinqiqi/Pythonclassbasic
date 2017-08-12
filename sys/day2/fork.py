#!/usr/bin/python

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print "create process failed"
elif pid == 0:
    print "This is child process:",os.getppid()
    while True:pass
else:
    sleep(0.1)
    print("parent process:",os.getpid())
    while True:pass

print "++++++++++++++++++++++++"
