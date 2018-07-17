# -*- coding:utf-8 -*-

from django.shortcuts import HttpResponse
from .models import *
from .recode import recode
from django.http import JsonResponse


# Create your views here.
# 返回文章列表
def article_list(request):

    data = articles.objects.filter(is_pub=True).order_by("-article_id").values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回文章详情
# 废弃接口
'''
def article_detail(request):

    get_id = request.GET.get('guid')

    data = articles.objects.filter(article_id=get_id).values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

'''


# 返回视频列表
def movie_list(request):

    data = movies.objects.filter(is_pub=True).order_by("-movie_id").values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response


# 返回音频列表
def audio_list(request):

    data = audios.objects.filter(is_pub=True).order_by("-audio_id").values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response


# 保存反馈信息
def feed_back(request):

    response = {'flag': False}

    if request.method == 'POST':

        question = request.POST.get("feedback")

        name = request.POST.get("name")

        phone = request.POST.get("phone")

    elif request.method == 'GET':

        question = request.GET.get("feedback")

        name = request.GET.get("name")

        phone = request.GET.get("phone")

    print(question, name, phone)

    try:
        models.feedbacks.objects.create(feedback=question, user_name=name, user_phone=phone)

        response['flag'] = True

        return JsonResponse(response)

    except:

        return JsonResponse(response)






# 返回视频详情
# 废弃接口
'''
def movie_detail(request):

    get_id = request.GET.get('guid')

    data = movies.objects.filter(article_id=get_id).values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

'''

# 返回banner信息
# 废弃接口
'''
def article_banner(request):

    data = articles.objects.all().order_by("-article_id")[0:5].values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response



def movie_banner(request):

    data = movies.objects.all().order_by("-movie_id")[0:6].values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response
'''