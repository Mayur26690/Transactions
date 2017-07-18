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
    total = 0
    for exp in all:
    	total += exp.movie
    	total += exp.hotel
    	total += exp.restaurent
    	total += exp.shopping
    	total += exp.sport
     

    return render(req,'amount/user.html',{'ans':ans, 'users':all, 'total':total})
def Datasheet(req):
    all = models.Spent.objects.order_by("movie")
    ans = "Order by Movie "
    total = 0
    for exp in all:
        total += exp.movie

    return render(req,'amount/movie.html',{'ans':ans, 'movies':all, 'total':total})

    
def Movie(req):
    all = models.Spent.objects.order_by("movie")
    ans = "Order by Movie "
    total = 0
    for exp in all:
    	total += exp.movie

    return render(req,'amount/movie.html',{'ans':ans, 'movies':all, 'total':total})

def Restaurant(req):
    all = models.Spent.objects.order_by("restaurant")
    ans = "Order by Resturant "
    total = 0
    for exp in all:
    	total += exp.restaurant
    return render(req,'amount/restaurant.html',{'ans':ans, 'restaurant':all,'total':total})

def Hotel(req):
    all = models.Spent.objects.order_by("hotel")
    ans = "Order by Hotel "
    total = 0
    for exp in all:
    	total += exp.hotel

    return render(req,'amount/hotel.html',{'ans':ans, 'hotel':all,'total':total})

def Shopping(req):
    all = models.Spent.objects.order_by("shopping")
    ans = "Order by Shopping "
    total = 0
    for exp in all:
    	total += exp.shopping

    return render(req,'amount/shopping.html',{'ans':ans, 'shopping':all,'total':total})

def Sport(req):
    all = models.Spent.objects.order_by("sport")
    ans = "Order by Sport "
    total = 0
    for exp in all:
    	total += exp.sport

    return render(req,'amount/sport.html',{'ans':ans, 'sport':all,'total':total})

def Total(req):
	all = models.Spent.objects.all()
	total = 0
	for exp in all:
		total += exp.movie
	return render(req,'amount/total.html',{'total':total})	