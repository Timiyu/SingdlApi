# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
import json
from . import models

# Create your views here.
def list(request):
    data = models.articles.objects.all()
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data), ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")

def detail(request):
    data = models.movies.objects.all()
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data), ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")