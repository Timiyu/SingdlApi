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
    data = json.dumps(json.loads(data), ensure_ascii=False)
    response = HttpResponse(data, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def article_detail(request):
    data = models.articles.objects.all()
    data = serializers.serialize('json', data, fields=('author', 'titile', 'content'))
    data = json.dumps(json.loads(data), ensure_ascii=False)
    response = HttpResponse(data, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def movie_list(request):
    data = models.movies.objects.all()
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data), ensure_ascii=False)
    response = HttpResponse(data, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def movie_detail(request):
    data = models.movies.objects.all()
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data), ensure_ascii=False)
    response = HttpResponse(data, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response