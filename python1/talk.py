#!/usr/bin/python

class Calculator(object):
    name = "luosifu"
    age = 88

class Talker(object):
    name = "mengfei"
    sex = 'man'


class TalkCalculator(Calculator,Talker):
    pass

A = TalkCalculator()

print A.age
print A.sex
print A.name

print TalkCalculator.__a__
