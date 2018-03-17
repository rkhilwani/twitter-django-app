# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    ptext = models.CharField(max_length=144)
    cdate = models.DateTimeField(auto_now=True)

class User(models.Model):
    username   = models.CharField(max_length=40)
    first_name = models.CharField(max_length=80)
    last_name  = models.CharField(max_length=80)
    email      = models.CharField(max_length=255)
    password   = models.CharField(max_length=20)