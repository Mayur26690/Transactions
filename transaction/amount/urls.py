from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^user/',views.User ),
    url(r'^movie/', views.Movie),
    url(r'^resturant/', views.Restaurant),
    url(r'^hotel/', views.Hotel),
    url(r'^shopping/', views.Shopping),
    url(r'^sport/', views.Sport),
    url(r'^total/', views.Total),
]