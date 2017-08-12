#!/usr/bin/python

from time import sleep
import os

try:
    os.mkfifo('fifo')
except OSError:
    print "fifo exist"



f = open('fifo','r')

while True:
    sleep(1)
    str = f.readline()
    print str
