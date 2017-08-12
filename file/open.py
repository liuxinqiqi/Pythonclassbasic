#coding=utf-8

try:
    f = open('file','r+')
except IOError as e:
    print e

print f

f.close()
print f

with open('file','r') as f:
    for i in f:
        print i,
