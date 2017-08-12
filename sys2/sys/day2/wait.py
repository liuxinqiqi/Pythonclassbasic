#!/usr/bin/python 

import os
from time import sleep


pid = os.fork()

if pid < 0:
    print "create process error"
elif pid == 0:
    print "child process ...."
    print os.getpid()
    sleep(4)
else:
    os.wait()
    print "parent process ...."
    while True:pass
    print pid
