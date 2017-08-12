#coding=utf-8

from django.conf.urls import url
from myapp.views import *

urlpatterns = [
    url(r'^first/$',first),
    url(r'^bs/$',bs),
    url(r'^test/$',test),
    url(r'^template/$',temp),
    url(r'^meta/$',display_meta),
    url(r'^tags/$',tag),
    url(r'^filter/$',fil),
    url(r'^base/$',base,name='base'),
    url(r'^include/$',nav),
    url(r'^static/$',load),
]

urlpatterns += [
    url(r'^models/$',mydb),
    url(r'^models1/$',mtm),
]
