from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.NewsletterSub, name='subscribe'),
    path('unsubscribe/', views.NewsletterUnsub, name='unsubscribe'),
]
