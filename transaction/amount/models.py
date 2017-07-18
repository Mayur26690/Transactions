# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class User(models.Model):
# 	last_name = models.CharField(max_length=20)
# 	first_name =  models.CharField(max_length=20)
# 	def __str__(self):
# 		return self.last_name

# class Spent(models.Model):

# 	movie = models.PositiveIntegerField(default = '0')
# 	hotel = models.PositiveIntegerField(default = '0')
# 	restaurent = models.PositiveIntegerField(default = '0')
# 	shopping = models.PositiveIntegerField(default = '0')
# 	sport = models.PositiveIntegerField(default = '0')
# 	user = models.OneToOneField(User)

# 	def __str__(self):
#  		return str(self.movie)

class Spent(models.Model):
	movie = models.PositiveIntegerField(default = '0')
	hotel = models.PositiveIntegerField(default = '0')
	restaurent = models.PositiveIntegerField(default = '0')
	shopping = models.PositiveIntegerField(default = '0')
	sport = models.PositiveIntegerField(default = '0')
	
