# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    read = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'book_info'


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField(default=True)
    content = models.TextField()
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)

    class Meta:
        db_table = 'hero_info'
