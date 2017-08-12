#!/usr/bin/python

import multiprocessing
from time import sleep
import os

def worker(sec):
    '''worker function'''
    sleep(sec)
    print "worker"
    return


p = multiprocessing.Process(target = worker,name = "myprocess",args = (3,))
p.start()
print "child:",p.pid
print "name:",p.name


#sleep(3)
p.join(1)
print "++++++++++++++++++++++++"
