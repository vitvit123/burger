from django.urls import include, re_path
from django.conf import settings 

from burgerapp import views as burgerapp_view
from . import views
from burgerapp.views import *
from django.urls import path
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from django.urls import re_path
from burgerapp import views

app_name = 'burgerapp'
urlpatterns = [
    # url('^home/$', staff_view.home_page, name='home'),
    re_path('^homepage/$', burgerapp_view.homepage, name='homepage'),
    re_path('^menupage/$', burgerapp_view.menu, name='menupage'),
    re_path('^promotionpage/$', burgerapp_view.promotion, name='promotionpage'),
    re_path('^aboutuspage/$', burgerapp_view.aboutus, name='aboutuspage'),
    re_path('^contactus/$', burgerapp_view.contactus, name='contactus'),
    re_path('^Newspage/$', burgerapp_view.news, name='news'),
    # re_path('^Signin/$', burgerapp_view.signin, name='signin'),
    re_path('signup/', views.signup, name='signup'),
]
