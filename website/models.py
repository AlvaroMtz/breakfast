# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.CharField(max_length=100, null=True)
    avatar = models.ImageField ()
    description = models.CharField(max_length=150, null=True)


class Post(models.Model):
    title = models.CharField(max_length=150, null=True)
    social_title = models.CharField(max_length=60, null=True)
    slug = models.SlugField(null=True)
    social_description = models.CharField(max_length=155, null=True)
    post = models.TextField(null=True)
    autor = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
