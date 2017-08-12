#!/usr/bin/python

class Parent(object):
    def __init__(self):
        self.job = "teacher"
        self.__name = 'cainiao'
        self.__score = 0

    def name(self,n):
        if n == 1:
            return self.__name
        else:
            return "sorry"

    def getName(self):
        return self.__name

    def setName(self,score):
        if score > 100 || score < 0:
            self.__score = 0
            return None
        else:
            self.__score = score


class Child(Parent):
    pass

# c = Child()
#
# print c.__name

p = Parent()
print p.job

print p.name(1)
