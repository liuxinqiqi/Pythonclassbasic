#!/usr/bin/python

import multiprocessing
from time import sleep
import sys
import subprocess

def daemon():
    f = open('daemon','w')
    p = multiprocessing.current_process()
    print('Starting:',p.name,p.pid)
    sys.stdout.flush()
    print('Exiting :',p.name,p.pid)
    sys.stdout.flush()
    while True:
        sleep(1)
        print >>f,'hello world\n'
        f.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:',p.name,p.pid)
    sys.stdout.flush()
    print('Exiting :',p.name,p.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name = 'daemon',target = daemon)
    d.daemon = True

    n = multiprocessing.Process(name = 'non-daemon',target = non_daemon)
    n.daemon = False

    d.start()
    sleep(1)
    n.start()
#    sleep(10)
