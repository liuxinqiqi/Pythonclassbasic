#coding=utf-8
import datetime

class Deco(object):
    def __init__(self,obj):
        self.func = obj
    def __call__(self,*args,**kwarg):
        print "现在时间"
        self.func(*args,**kwarg)


@Deco
def getTime(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()


#begin(getTime)()
getTime(6,7,8,9)
