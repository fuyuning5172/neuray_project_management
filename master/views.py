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
        person.delete_time = datetime.datetime.now()
        print(datetime.datetime.now())
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

# 增加项目信息
# 修改项目信息
# 删除项目信息
# 查询项目信息列表


# 增加计划信息
# 修改计划信息
# 删除计划信息
# 查询计划信息列表


# 增加阶段信息
# 修改阶段信息
# 删除阶段信息
# 查询阶段信息列表