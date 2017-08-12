#!/usr/bin/python

from multiprocessing import Process,Queue

import time

q = Queue()

q.put("hello")
q.put("world")

print q.full()

print q.empty()

print q.qsize()

print q.get()
print q.qsize()
