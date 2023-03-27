from django.shortcuts import render, get_object_or_404
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
     path('', views.index, name='index'),
     path('contact/', views.contact, name='contact'),
     path('signup/', views.signup, name='signup'),
]