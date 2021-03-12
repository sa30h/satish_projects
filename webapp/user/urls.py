from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('home/',views.home ),
    path('login/',views.user_login),
]