#!/usr/bin/python

import multiprocessing
from time import sleep
import os

def worker(sec):
    '''worker function'''
    p = multiprocessing.current_process()
    i = 0
    while True:
        sleep(sec)
        print "worker"
        i += 1
    print "in child process :",p.pid
    print "in child process :",os.getppid()
    return


p = multiprocessing.Process(target = worker,name = "myprocess",args = (1,))
p.start()
print "child:",p.pid
print "name:",p.name



print os.getpid()
