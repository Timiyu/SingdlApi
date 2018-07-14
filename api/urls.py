"""Singdlapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('movie_list/', views.movie_list, name='movie_list'),
    #path('article_detail/', views.article_detail, name='articel_detail'), 废弃
    path('movie_detail/', views.movie_detail, name='movie_detail'),
    path('article_banner/', views.article_banner, name='article_banner'),
    #path('movie_banner/', views.movie_banner, name='movie_banner'),废弃
]
