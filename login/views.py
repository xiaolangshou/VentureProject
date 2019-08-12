from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.contrib import messages

import time

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        print(request.method, request.POST)
        if user == "liutao" and pwd == "12345":
            return render(request, "index.html")
        else:
            return render(request, "login.html")


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
