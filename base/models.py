from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    db_table = 'user'
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    db_table = 'article'
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=64)
    addtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    description = models.CharField(max_length=255)
    content = models.TextField()
    tag = models.CharField(max_length=255)
    categoryid = models.IntegerField()
    def __unicode__(self):
        return self.name

class Category(models.Model):
    db_table = 'category'
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    order = models.IntegerField()
    # addtime = models.DateTimeField(default=datetime.datetime.now().date)
    # addtime = models.DateTimeField(auto_now_add=True)
    addtime = models.DateTimeField()
    pid = models.IntegerField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    db_table = 'tag'
    name = models.CharField(max_length=255)
    addtime = models.DateTimeField()
    def __unicode__(self):
        return self.name