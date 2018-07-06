# -*- coding:utf-8 -*-

from django.core import serializers
import json

def recode(data):
    data = serializers.serialize('json', data)
    data = json.dumps(json.loads(data), ensure_ascii=False)
    return data
