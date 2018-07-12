# -*- coding:utf-8 -*-

from django.shortcuts import HttpResponse
from .models import *
from .recode import recode


# Create your views here.
# 返回文章列表
def article_list(request):

    data = articles.objects.filter(is_pub=True).order_by("-article_id").all().values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回文章详情
def article_detail(request):

    get_id = request.GET.get()

    data = articles.objects.filter(id=get_id).values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回视频列表
def movie_list(request):

    data = movies.objects.all().values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回视频详情
def movie_detail(request):

    get_id = request.GET.get()

    data = movies.objects.filter(id=get_id).values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response