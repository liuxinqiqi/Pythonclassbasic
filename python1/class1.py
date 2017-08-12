#!/usr/bin/python
#coding=utf-8

class Person(object):
#    print "This is a class"
    def __init__(self,name):
        self.name = name

    age = 10
    print age
    def color(self,c):
        print "%s is %s,he is %d"%(self.name,c,self.age)
#        print self.face

boy1 = Person("Jame")

boy1.age = 12

print boy1.age

print boy1.name

boy1.face = "帅"

boy1.color("black")
print boy1.face

print "=================================="
boy2 = Person("Lilei")

print boy2.age

print boy2.name


boy2.color("black")

print "=========================================="


print Person.age

#print Person.face
