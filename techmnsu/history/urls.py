from django.contrib import admin
from django.urls import path
from . import views as history_views

urlpatterns = [
    path('history/', history_views.history, name = 'history'),
]