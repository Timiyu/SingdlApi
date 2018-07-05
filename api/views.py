# -*- coding:utf-8 -*-
from django.core import serializers
from django.shortcuts import HttpResponse
from django.shortcuts import render
from . import models
import json


# Create your views here.
# 返回文章列表
def article_list(request):
    data = models.articles.objects.all()

    data = serializers.serialize('json', data, fields=('article_id', 'author', 'title', 'comment', 'article_coverimg'))

    data = json.dumps(json.loads(data), ensure_ascii=False)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回文章详情
def article_detail(request):

    data = models.articles.objects.all()

    data = serializers.serialize('json', data, fields=('article_id', 'author', 'title', 'content'))

    data = json.dumps(json.loads(data), ensure_ascii=False)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回视频列表
def movie_list(request):

    data = models.movies.objects.all()

    data = serializers.serialize('json', data)

    data = json.dumps(json.loads(data), ensure_ascii=False)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回视频详情
def movie_detail(request):

    data = models.movies.objects.all()

    data = serializers.serialize('json', data)

    data = json.dumps(json.loads(data), ensure_ascii=False)

    response = HttpResponse(data, content_type="application/json")

    return response