# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import emailView, successView

urlpatterns = [
    path('', emailView, name='emailView'),
    path('success/', successView, name='successView'),
    ]