# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
import json
from . import models

# Create your views here.
def list(request):
    data = models.articles.objects.all()
    print(data)
    data = serializers.serialize('json', data)
    print(data)
    return HttpResponse(data, content_type="application/json")

def detail(request):
    data = models.movies.objects.all()
    data = serializers.serialize('json', data)
    print(data)
    return HttpResponse(data, content_type="application/json")