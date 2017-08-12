#coding=utf-8

from django.conf.urls import url
from formapp.views import *

urlpatterns = [
    url(r'^search-form/$',search_form),
    url(r'^search/$',search),
]

urlpatterns += [
    url(r'^contact/$',contact),
    url(r'^contact/thanks',thanks),
]


urlpatterns += [
    url(r'^form/$',formtest),
    url(r'^bookform/$',bookset),

]
