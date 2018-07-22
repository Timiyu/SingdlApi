# -*- coding:utf-8 -*-

from django.shortcuts import HttpResponse
from api.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.recode import *
from api.comre import *
from api.sendcode import send_message
from api.createcode import create_code
import json




# Create your views here.
# 返回文章列表
def article_list(request):

    data = articles.objects.filter(is_pub=True).order_by("-article_id").values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response

# 返回文章详情
# 废弃接口

def article_detail(request):

    get_id = request.GET.get('guid')

    data = articles.objects.filter(article_id=get_id).values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response




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
@csrf_exempt
def feed_back(request):

    response = {'flag': 0}   # 初始状态

    if request.method == 'POST':

        post_data = json.loads(request.body)

        question = post_data['feedback']

        name = post_data['name']

        phone = post_data['phone']

        if len(question) == 0:

            response['flag'] = 1    # 反馈内容为空

            return JsonResponse(response)

        elif namecheck(name)!=True:

            response['flag'] = 2    # 姓名非法

            return JsonResponse(response)

        elif phonecheck(phone)!=True:

            response['flag'] = 3    # 手机号非法

            return JsonResponse(response)

        else:

            try:

                feedbacks.objects.create(feedback=question, user_name=name, user_phone=phone)

                response['flag'] = 4    # 入库成功

                return JsonResponse(response)

            except:

                response['flag'] = 0

                return JsonResponse(response)   # 重置为初始状态


# 发送短信验证码
@csrf_exempt
def get_send_msgcode(request):

    response = {'flag': 0, 'code': ''}   # 初始状态



    if request.method == 'POST':

        post_data = json.loads(request.body)

        phone = post_data['phone']

        code = ''

        if phonecheck(phone)!=True:

            response['flag'] = 3    # 手机号非法

            return JsonResponse(response)   # 返回错误信息

        else:

            try:
                code = create_code()

                backcode = send_message(phone, code)

                if backcode['error'] == 0:

                    response['flag'] = 1    # 发送成功

                return JsonResponse(response)           # 返回code

            except:

                response['flag'] = 2

                return JsonResponse(response)   # 重置为初始状态

'''

# 返回视频详情
# 废弃接口

def movie_detail(request):

    get_id = request.GET.get('guid')

    data = movies.objects.filter(article_id=get_id).values()

    data = recode(data, isAscii=True)

    response = HttpResponse(data, content_type="application/json")

    return response



# 返回banner信息
# 废弃接口

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
