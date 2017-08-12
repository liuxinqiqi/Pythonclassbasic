#! /usr/bin/python 

import sys
import time

l = []
try:
     p = open(sys.argv[1],'r')
     count = len(p.readlines())
     i = count + 1
     w = open(sys.argv[1],'a')
except IOError,e:
     w = open(sys.argv[1],'w')
     i = 1

while True:
     t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
     l.append(i)
     l.append(',')
     l.append(t)
     l.append('\n')
     time.sleep(1)
     l = map(str,l)
     w.writelines(l)
     i += 1
     l = []
