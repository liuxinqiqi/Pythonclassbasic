#!/usr/bin/python

with open('hold','w') as f:
    f.write('begin')
    f.seek(1000,2)
    f.write('end')
