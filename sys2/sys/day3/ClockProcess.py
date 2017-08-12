#!/usr/bin/python

import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self,value):
        multiprocessing.Process.__init__(self)
        self.value = value

    def run(self):
        n = 5
        while n > 0:
            print "the time is {}".format(time.ctime())
            time.sleep(self.value)
            n -= 1

p = ClockProcess(3)

p.start()

while True:
    time.sleep(1)
    print "+++++++++++++"
