# -*- coding:utf-8 -*-
from django.core import serializers
from django.shortcuts import HttpResponse
from .models import *
import json
from .recode import recode


# Create your views here.
# 返回文章列表
def article_list(request):

    data = articles.objects.all().values()

    data = recode(data)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回文章详情
def article_detail(request):

    data = articles.objects.all().values()

    data = recode(data)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回视频列表
def movie_list(request):

    data = movies.objects.all().values()

    data = recode(data)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回视频详情
def movie_detail(request):

    data = movies.objects.all().values()

    data = recode(data)

    response = HttpResponse(data, content_type="application/json")

    return response