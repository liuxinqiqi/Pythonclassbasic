#!/usr/bin/python

import multiprocessing
from time import sleep
import os


def worker(msg):
    print os.getpid()
    while True:
        sleep(2)
        print msg
    return

if __name__ == '__main__':
    p = multiprocessing.Pool(processes = 4)
    result = []
    for i in xrange(10):
        msg = "hello %d"%(i)
        result.append(p.apply_async(worker,(msg,)))
    
    for res in result:
        print res.get()
