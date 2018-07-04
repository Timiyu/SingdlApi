# -*- coding:utf-8 -*-
from django.core import serializers
from django.shortcuts import HttpResponse
from django.shortcuts import render
from . import models
import json


# Create your views here.
def article_list(request):
    data = models.articles.objects.all()
    data = serializers.serialize('json', data, fields=('author', 'title', 'comment', 'article_coverimg'))
    print(data)
    data = json.dumps(json.loads(data), ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")

def article_detail(request):
    data = models.articles.objects.all()
    data = serializers.serialize('json', data, fields=('author', 'titile', 'content'))
    data = json.dumps(json.loads(data), ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")

def movie_list(request):
    data = models.movies.objects.all()
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data),ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")

def movie_detail(request):
    data = models.movies.objects.all()
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data),ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")