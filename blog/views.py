from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hello(request):
    name = '刘涛的教程'
    books = ['Python学习手册', 'Python核心编程', 'PythonCookBook']
    myDict = {"name": 'liutao', 'age': 28}
    return render(request, 'hello.html', {'name': name, 'books': books, 'dict': myDict})
