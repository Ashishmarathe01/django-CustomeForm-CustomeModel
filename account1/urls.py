from django.contrib import admin
from django.urls import path, include
from .views import signup,login_view,home

urlpatterns = [
    path('',signup,name='reg'),
    path('login',login_view,name='login'),
    path('home',home,name='home')

]