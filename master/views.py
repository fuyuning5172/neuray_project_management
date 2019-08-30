import os

from django.http import HttpResponse
from django.shortcuts import render
from master import models

# Create your views here.
# def main(request):
#     render(request,"main.html")

#登录
def index(request):
    return render(request, "login.html")


def login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == "123":
            return render(request, 'main.html')
        else:
            return render(request, 'login.html', context={"res": "管理员密码错误"})

#测试
def test(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        department = request.POST.get('department')
        change = models.Person(personnel_name=person_name, department=department)
        change.save()
        return HttpResponse('ok')
    else:
        return render(request, "test.html")
