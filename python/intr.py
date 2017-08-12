#coding=utf-8

#hasattr  getattr setattr delattr isinstance  issubclass


class Parent(object):
    name = 'FangKun'

class Child(Parent):
    pass


p = Parent()
print issubclass(Child,Parent)
print isinstance(p,Parent)

print "============================================"

print hasattr(p,'name')

print getattr(p,'name')

#setattr(p,'age',23)

p.age = 23

delattr(p,'age')

#print p.age
