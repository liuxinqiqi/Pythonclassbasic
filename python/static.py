#coding=utf-8

class TestStaticMethod(object):
    @staticmethod
    def foo():
        print "calling static method foo()"

    #foo = staticmethod(foo)

class Child(TestStaticMethod):
    pass

static = TestStaticMethod()

static.foo()
TestStaticMethod.foo()


child = Child()

child.foo()

print "==============================================="
class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print "calling class method foo()"
        print cls.__name__

class Child1(TestClassMethod):
    pass

cls = TestClassMethod()

cls.foo()
TestClassMethod.foo()


child = Child1()

child.foo()
