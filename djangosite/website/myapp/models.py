# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BookQuerySet(models.QuerySet):
    def little(self):
        return self.filter(id__lt = 4)

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model,using=self._db)

    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()


class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField(verbose_name = "网址")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        ordering = ['name']
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField(null = True,default = 10)
    email = models.EmailField(blank = True)

    def __unicode__(self):
        return "%s %s"%(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    publication_date = models.DateField(blank = True,null = True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    objects = models.Manager()
    myobjects = BookManager()
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
