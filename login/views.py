from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

import time


# Create your views here.
def login(request):
    print(request.META)
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    request.session["username"] = username

    print(username, type(username))
    print(password, type(password))

    if username == "liutao" and password == "12345":
        return HttpResponse("登录成功!")
    else:
        return HttpResponse("未知!")

    # return HttpResponseRedirect('/index')


def index(request):
    print(request.META)
    username = request.session.get("username", "err")
    s = '欢迎你： %s, <a herf="/home">跳转个人页面</a>' % username
    return HttpResponse(s)


def home(request):
    username = request.session.get("username", 'err')
    s = 'this is %s home page! <a href="/logout">安全退出</a>' % username
    return HttpResponse(s)


def logout(request):
    request.session.clear()
    s = '你已经安全退出！'
    return HttpResponse(s)


def add(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    return HttpResponse("a + b = %s" % (a + b))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse("Total is %s" % c)


@cache_page(3)
def cache(request):
    x = time.time()
    return HttpResponse(x)
