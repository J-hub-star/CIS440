from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'rental-home'),
    path('about/', views.about,name = 'rental-about'),
    path('profile/user_id/', views.profile,name = 'rental-profile')

]
