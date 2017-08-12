#!/usr/bin/python
#coding=utf-8
class A(object):
    attr = None

class B(A):
    pass

a = A()
a.name = "new"
b = B()

print dir(a)
print  a.name
# delattr(a,'name')  # 只能删除似有属性   等价于  del a.name
# print dir(a)
# print  a.name
print hasattr(a,'name')

print getattr(a,'attr')

print issubclass(B,A)

print isinstance(a,A)
print isinstance(b,A)

print type(a)
