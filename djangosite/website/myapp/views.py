# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template import loader,RequestContext
import time
from myapp.models import *
from django.db.models import F,Q
import datetime

# Create your views here.

def global_setting(request):
    NAME = 'cainiao'
    TEL = '18810207835'
    GEYAN = '业精于勤而荒于嬉，行成于思而毁于随'

    return locals()

def fun():
    return "hello"

class A(object):
    a = "class->a"
    def f(self):
        return "jest a A:fun"

def first(request):
    return HttpResponse("my first app")

def bs(request):
    t = loader.get_template('bs.html')
    html = t.render({})
    return HttpResponse(html)

def test(request):
    #return render_to_response('bs.html',{})
    return render(request,'bs.html',{})

def temp(request):
    datetime = time.localtime()
    #return render(request,'time.html',{'datetime':t})
    return render(request,'time.html',locals())

def display_meta(request):
    num = 1
    s = "hello"
    l = [1,2,'c','nihao']
    t = (4,5,'d','tuple')
    d = {'a':'one','b':'two','c':'three'}
    f = fun()
    obj = A()

    return render(request,'meta.html',\
    {'num':num,'s':s,'list':l,'tuple':t,'dict':d,'fun':f,'obj':obj})

def tag(request):
    error = "error"
    l = [1,2,3,4]
    return render(request,'tags.html',{'error':error,'list':l})

def fil(request):
    num = 1
    s = "HELLO WORLD"

    return render(request,'filter.html',{'num':num,'s':s})


def base(request):
    return render(request,'extent.html',{})

def nav(request):
    return render(request,'nav.html',{})
    #return render_to_response('nav.html',{},context_instance=RequestContext(request))
def load(request):
    return render(request,'static.html',{})

def mydb(request):
    # #增1
    Author.objects.create(first_name = 'Jame',last_name = "Green",email = 'jm@123.com')
    Publisher.objects.create(name = "人民",address = "beijing",city = "beijing",state_province = "haidian",country = "China",website = 'http://192.168.1.1')
    Book.objects.create(title = "Python Book",publication_date=datetime.datetime.now(),publisher_id = 1)
    Book.objects.create(title = "HTML5",publication_date=datetime.datetime.now(),publisher_id = 1)
    Book.objects.create(title = "JavaScript",publication_date=datetime.datetime.now(),publisher_id = 1)




    #增2
    obj = Author(first_name = 'Han',last_name = "mei",email = 'hm@123.com')
    obj.save()

    dic = {'first_name' : 'Lei','last_name' : "Li",'email' : 'hm@123.com'}
    obj = Author(**dic)
    obj.save()



    #查 select * from author

    a = Author.objects.all()  #每一条记录生成一个对象
    b = Author.objects.all().values('email') #取出所有记录的指定字段
    c = Author.objects.all().values_list('first_name','email') #取出所有记录的指定字段
    #d = Author.objects.get(id=1) # 获取某一记录的对象
    e = Author.objects.filter(id= 1) # 获取某一记录的对象

    # Author.objects.filter().update(age = F('age') + 1)
    #
    # q = Q()
    # print dir(q)
    #
    # q.connector = 'AND'
    # q.children.append(('id',3))
    # q.children.append(('last_name','mei'))
    #
    # f = Author.objects.filter(q)

    return HttpResponse("OK")

def mtm(request):
    book1 = Book.objects.get(id = 2)
    s = book1.publisher.name

    pub1 = Publisher.objects.get(id = 1)
    book_list = pub1.book_set.all()

    author1 = Author.objects.get(id = 1)
    book1_list = author1.book_set.all()

    author_list = book1.author.all()

    book2_list = Book.myobjects.all().little()

    return HttpResponse(book2_list)
