# coding=utf-8
import datetime

def deco(arg):
    def begin(func):
        def wrapper(*args,**kwargs):
            print arg
            print "现在时间："
            func(*args,**kwargs)
        return wrapper
    return begin

@deco('deoc')
def getTime(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()


#begin(getTime)()
getTime(6,7,8,9)
