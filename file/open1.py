#coding=utf-8
import sys

with open('file1','r+') as f:
    print >>f,"撑着油纸伞，独自彷徨，彷徨在那悠长的雨巷"

print >>sys.stdout,"撑着油纸伞，独自彷徨，彷徨在那悠长的雨巷"
print >>sys.stderr,"撑着油纸伞，独自彷徨，彷徨在那悠长的雨巷"
print >>sys.stdin,"撑着油纸伞，独自彷徨，彷徨在那悠长的雨巷"
