from django.conf.urls import url
from base.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^info/$', info),
    url(r'^login/$', login),
    url(r'^category_add/$', category_add),
    url(r'^category_list/$', category_list),
    url(r'^category_delete/(?P<id>[0-9]+)', category_delete),
    url(r'^category_edit/(?P<id>[0-9]+)', category_edit),
    url(r'^tag_list/$', tag_list),
    url(r'^tag_add/$', tag_add),
    url(r'^tag_delete/(?P<id>[0-9]+)', tag_delete),
    url(r'^tag_edit/(?P<id>[0-9]+)', tag_edit),
    url(r'^article_add/$', article_add),
    url(r'^article_list/$', article_list),
    url(r'^article_edit/(?P<id>[0-9]+)', article_edit),
    url(r'^article_delete/(?P<id>[0-9]+)', article_delete),
]