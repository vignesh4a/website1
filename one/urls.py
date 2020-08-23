from django.contrib import admin
from django.urls import path,include
from one import views

app_name='one'

urlpatterns = [
path('',views.index,name="index"),
path('events/',views.events,name="events"),
path('resources/',views.resources,name="resources"),
path('about/',views.about,name="about"),

]
