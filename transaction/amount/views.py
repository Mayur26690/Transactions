# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db.models import Sum


# Create your views here.
def Datasheet(req):
    all = models.Spent.objects.all()
    ans = "Balance sheet"
    movie_total = models.Spent.objects.aggregate(Money_spent_on_movie=Sum('movie'))
    hotel_total = models.Spent.objects.aggregate(Money_spent_on_hotel=Sum('hotel'))
    restaurent_total = models.Spent.objects.aggregate(Money_spent_on_restaurent=Sum('restaurent'))
    shopping_total = models.Spent.objects.aggregate(Money_spent_on_shopping=Sum('shopping'))
    sport_total = models.Spent.objects.aggregate(Money_spent_on_sport=Sum('sport'))

    final_total = models.Spent.objects.all().aggregate(Total_money_spent=Sum('movie')+Sum('hotel')+Sum('restaurent')+Sum('shopping')+Sum('sport'))

    return render(req,'amount/hotel.html',{'ans':ans, 'spent':all, 'movie_total':movie_total,
        'hotel_total':hotel_total,'restaurent_total':restaurent_total,'shopping_total':shopping_total,'sport_total':sport_total,'final_total':final_total})