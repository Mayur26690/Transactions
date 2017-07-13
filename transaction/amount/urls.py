from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^user/',views.User ),
    url(r'^movie/', views.Movie),
    url(r'^resturant/', views.Restaurant),
]