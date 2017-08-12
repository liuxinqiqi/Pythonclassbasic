#!/usr/bin/python
#coding=utf-8

import sys

l = ['hi','hello','你好','sawadika']

try:
    f = open(sys.argv[1],'w+')
    f.write("hello world\n")
    f.writelines(l)
except IOError as e:
    print e
