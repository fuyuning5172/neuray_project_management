import os
import time
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from master import models


# 登录
def index(request):
    return render(request, "login.html")


def login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == "123":
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', context={"res": "管理员密码错误"})


# 测试
def test(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        department = request.POST.get('department')
        change = models.Person(personnel_name=person_name, department=department)
        change.save()
        return HttpResponse('ok')
    else:
        return render(request, "test.html")


# 增加人员信息
def add_person(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        department = request.POST.get('department')
        data = models.Person(personnel_name=person_name, department=department)
        data.save()
        return HttpResponse('ok')
    elif request.method == "GET":
        return render(request, "test.html")


# 修改人员信息
def update_person(request):
    if request.method == "GET":
        person_id = request.GET.get('person_id')
        person = models.Person.objects.get(personnel_id=person_id)
        person.save()
        return render(request, "update.html",context={{"update_person":person}})
    else:
        person_id = request.GET.get('person_id')
        person = models.Person.objects.get(personnel_id=person_id)


# 删除人员信息
def delete_person(request):
    if request.method == "GET":
        person = models.Person.objects.get(personnel_id='1')
        person.is_delete = 1
        person.delete_time = time.time()
        print(datetime.datetime)
        person.save()
        return HttpResponse('delete!')
    elif request.method == "GET":
        return render(request, "test.html")
#展示人员
def search_person(request):
    if request.method == "GET":
        personlist = models.Person.objects.all()
        print(personlist[0].personnel_name,"_______________")
        data = models.Person(personnel_name='ceshiname', department="ceshidep")
        data.save()
        return render(request, "person.html",context={"personlist":personlist})

