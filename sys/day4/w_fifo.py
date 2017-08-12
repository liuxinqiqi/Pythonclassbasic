#!/usr/bin/python

from time import sleep
import os,sys
from signal import *


pid = os.fork()

if pid < 0:
    print "create fifo failed"
    
elif pid == 0:
    try:
        os.mkfifo('w_fifo')
    except OSError:
        pass

    f_r = open('w_fifo','r')

    while True:
        str = f_r.readline()
        print str
        sys.stdout.flush()
else:
    signal(SIGCHLD,SIG_IGN)
    
    try:
        os.mkfifo('r_fifo')
    except OSError:
        pass
    
    f_w = open('r_fifo','w')

    while True:
        str = sys.stdin.readline()
        f_w.write(str)
        f_w.flush()


