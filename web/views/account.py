from django.shortcuts import render, redirect
from web import models

from utils.encrypt import md5


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = md5(request.POST.get("password"))
    role = request.POST.get("role")
    print(username, password)

    # 校验
    mapping = {"1": "ADMIN", "2": "CUSTOMER"}
    if role not in mapping:
        return render(request, "login.html", {"error": "角色不存在"})
    if role == "1":
        user_object = models.Administrator.objects.filter(active=1, username=username, password=password).first()
    else:
        user_object = models.Customer.objects.filter(active=1, username=username, password=password).first()
    if not user_object:
        return render(request, "login.html", {"error": "用户名或密码错误"})

    request.session['user_info'] = {'role': mapping[role], 'name': user_object.username, 'id': user_object.id}
    return redirect("/home/")


def sms_login(request):
    return render(request, "sms_login.html")
