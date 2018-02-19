
import os
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sportsman_id>[0-9]+)/tap$', views.tapSportsman, name='tapSportsman'),
    url(r'^Start$', views.tapStart, name='tapStart'),
    url(r'^Results$', views.GetResults, name='GetResults'),
    url(r'^Test$', views.GetTest, name='GetTest'),
    url(r'^login/$', views.GetLogin, name='GetLogin'),
    url(r'^login/tapLogin$', views.tapLogin, name='tapLogin'),
    url(r'^logout/$', auth_views.logout, {'next_page': '../Results'}, name='logout'),
]

