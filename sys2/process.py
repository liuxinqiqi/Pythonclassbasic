#!/usr/bin/python

import multiprocessing
from time import sleep
import os


def worker(sec):
    print "parent pid:",os.getppid()
    while True:
        sleep(sec)
        print "worker...."
    return

if __name__ == '__main__':
    p = multiprocessing.Process(target = worker,name = "myprocess",args = (3,))
    p.start()
    print os.getpid()
