# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
# def all_movie(req):
# 	allMovie = models.Spent.objects.all()
# 	text = "All transactions"

# 	return render(req, "amount/movie.html",{'movie':allMovie, 'text':text})

def User(req):
    all = models.Spent.objects.all()
    ans = "All Users Monthly Expenses"

    return render(req,'amount/user.html',{'ans':ans, 'users':all})

def Movie(req):
    all = models.Spent.objects.order_by("movie")
    ans = "Order by Movie "

    return render(req,'amount/movie.html',{'ans':ans, 'movies':all})

def Restaurant(req):
    all = models.Spent.objects.order_by("restaurant")
    ans = "Order by Resturant "

    return render(req,'amount/restaurant.html',{'ans':ans, 'restaurant':all})

def Hotel(req):
    all = models.Spent.objects.order_by("hotel")
    ans = "Order by Hotel "

    return render(req,'amount/hotel.html',{'ans':ans, 'hotel':all})

def Shopping(req):
    all = models.Spent.objects.order_by("shopping")
    ans = "Order by Shopping "

    return render(req,'amount/shopping.html',{'ans':ans, 'shopping':all})

def Sport(req):
    all = models.Spent.objects.order_by("sport")
    ans = "Order by Sport "

    return render(req,'amount/sport.html',{'ans':ans, 'sport':all})