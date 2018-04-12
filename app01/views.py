from django.shortcuts import render, HttpResponse
from django.views import View

from app01.models import *


def add(request):  # 价格策略表添加数据
    # Pricepolicy.objects.create(content_type=7, object_id=1, period='1个月', price=9.9)
    # 课程数据对象包含 id和表名, 就不用contentType, object_id了
    course_obj = Course.objects.get(id=1)
    Pricepolicy.objects.create(period='1个月', price=9.9, content_object=course_obj)
    Pricepolicy.objects.create(period='2个月', price=99, content_object=course_obj)
    Pricepolicy.objects.create(period='3个月', price=999, content_object=course_obj)

    return HttpResponse('ok')


def list_1(request):  # 查询价格策略表所有的价格,周期,课程
    policy_list = Pricepolicy.objects.all()
    for obj in policy_list:
        print("周期:",obj.period, "价格:",obj.price, "数据对象:",obj.content_object)
    return HttpResponse('ok')

# 但是实际应用往往是给你一个课程,去查询这个课程的周期,价格

def list_2(request):
    course_obj = Course.objects.get(id=1)
    policy_list = course_obj.policy_list.all()
    print(policy_list)
    return HttpResponse('ok')

def index(request):
    import json
    response = HttpResponse(json.dumps({"status": True, "data": "seven"}))
    # response["Access-Control-Allow-Origin"] = "*"   # 所有跨域访问都允许通过
    response["Access-Control-Allow-Origin"] = "http://localhost:63342"   # 所有跨域访问都允许通过
    response["Access-Control-Allow-Methods"] = "PUT, DELETE"  # 允许请求方式
    response["Access-Control-Allow-Headers"] = "k1, k2"     # 允许请求头


    # response["Access-Control-Max-Age"] = 5  # 第一次访问后,5秒钟内不做预检


    response["Access-Control-Expose-Headers"] = "game_over"
    response["game_over"] = "Hello World!"

    response["Access-Control-Allow-Credentials"] = 'true'
    response.set_cookie('key33', "value33", max_age=5)
    return response

