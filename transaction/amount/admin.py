# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Spent
# Register your models here.

class SpentAdmin(admin.ModelAdmin):
	list_display = ('movie', 'hotel', 'restaurent','shopping','sport')
	ordering = ['movie','hotel']
admin.site.register(Spent, SpentAdmin)
