#!/usr/bin/python

import multiprocessing
from time import sleep
import os

def worker(sec):
    '''worker function'''
    while True:
        sleep(sec)
        print "worker"
    return


p = multiprocessing.Process(target = worker,name = "myprocess",args = (3,))
p.start()
print "child:",p.pid
print "name:",p.name
print "is_alive",p.is_alive()



print os.getpid()
