import os

from django.http import HttpResponse
from django.shortcuts import render
from master import models

# Create your views here.
# def main(request):
#     render(request,"main.html")


def index(request):
    return render(request, "login.html")


def login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == "123":
            return render(request, 'main.html')
        else:
            return render(request, 'login.html', context={"res": "管理员密码错误"})


def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        my_file =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not my_file:
            return HttpResponse("没有文件")
        shuju = open(os.path.join("F:\\upload", my_file.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for data in my_file.chunks():      # 分块写入文件
            shuju.write(data)
            shuju.close()
        return render(request, "ok.html")


def test(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        department = request.POST.get('department')
        change = models.Person(personnel_name=person_name, department=department)
        change.save()
        return HttpResponse('ok')
    else:
        return render(request, "test.html")
