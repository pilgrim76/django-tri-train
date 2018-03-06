
import os
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sportsman_id>[0-9]+)/tap$', views.tapSportsman, name='tapSportsman'),
    url(r'^(?P<sportsman_id>[0-9]+)/tapFinish$', views.tapSportsmanFinish, name='tapSportsmanFinish'),
    url(r'^(?P<distance_id>[a-zA-Z0-9][a-zA-Z0-9-_]*)/Start$', views.tapStart, name='tapStart'),
    url(r'^s24Results$', views.Gets24Results, name='Gets24Results'),
    url(r'^login/$', views.GetLogin, name='GetLogin'),
    url(r'^login/tapLogin$', views.tapLogin, name='tapLogin'),
    url(r'^logout/$', auth_views.logout, {'next_page': '../Results'}, name='logout'),
]

