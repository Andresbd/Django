# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name= models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    notes = models.TextField()
 
class Role_Type(models.Model):
    role = models.CharField(max_length = 200);

class Genre(models.Model):
    genre = models.CharField(max_length = 100)

class Title(models.Model):
    title = models.CharField(max_length = 100)
    story = models.TextField()
    release_date = models.DateTimeField('date published')
    duration = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class Actor_Roles(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role_type = models.ForeignKey(Role_Type, on_delete=models.CASCADE)
    character_name = models.CharField(max_length = 200)
    character_description = models.TextField()

class Producer(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 254)
    web_site = models.CharField(max_length = 200)

class Title_Producer(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
