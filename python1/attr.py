class A(object):
    def __getattr__(self, name):
        print "You use getattr no attr %s"%name
        return "NO"

    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value

    def __delattr__(self,name):
        print "You use delattr"

a = A()

print a.k
a.x = "set x"

del a.k
