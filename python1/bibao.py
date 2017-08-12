#coding=utf-8
#装饰器的概念:对函数(参数,返回值等)进行加工处理,生成一个功能增强版的一个函数。
#闭包就是根据不同的配置信息得到不同的结果.装饰器就是一种闭包
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()

# def out():
#     a = 1
#     def inner():
#         print a
#         print "I'm inner"
#     return inner
#
# f = out()
# f()
#
#
# def func(name):
#     def inner_func(age):
#         print 'name:', name, 'age:', age
#     return inner_func
#
# b = func('the 5 fire')
# b(26)
