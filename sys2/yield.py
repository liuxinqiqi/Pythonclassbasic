#!/usr/bin/python

import time
import sys

def produce(l):
    i = 0
    while True:
        if i < 5:
            l.append(i)
            yield i
            i += 1
            time.sleep(1)
        else:
            return

def consume(l):
    p = produce(l)
    while True:
        try:
            p.next()
            while len(l) > 0:
                print l.pop()
        except StopIteration:
            sys.exit(0)

l = []
consume(l)
