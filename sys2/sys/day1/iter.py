#!/usr/bin/python

with open('file','r') as f:
    f_dict = f.readlines()
    list_iter = iter(f_dict)
    try:
        while True:
            print list_iter.next()
    except:
        print "stop!!!"
