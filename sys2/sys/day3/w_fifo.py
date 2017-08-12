#!/usr/bin/python

from time import sleep
import os

try:
    os.mkfifo('fifo')
except OSError:
    print "fifo exist"

f = open('fifo','w')

while True:
    sleep(1)
    f.write('hello\n')
    f.flush()
    

