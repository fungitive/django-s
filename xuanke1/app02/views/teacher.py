#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wangj
from django.shortcuts import render,HttpResponse,redirect
from app02 import models
def get_teacher(request):#查询到老师页面
    teacher_list=models.Teacher.objects.all()
    return render(request, 'get_teacher.html', {"teacher_list":teacher_list})
def add_teacher(request):#添加老师
    if request.method=="GET":
        return render(request, "add_teacher.html")
    elif request.method=="POST":
        name=request.POST.get('name')
        models.Teacher.objects.create(name=name)
        return redirect("/teacher.html")#跳转到url路径
    else:
        return render(request, "add_teacher.html")

def delete_teacher(request):
    nid=request.GET.get('nid')
    models.Teacher.objects.filter(id=nid).delete()
    return  redirect("/teacher.html")
def edit_teacher(request):
    if request.method=="GET":
        nid = request.GET.get('nid')
        obj = models.Teacher.objects.filter(id=nid).first()
        return render(request, "edit_teacher.html",{"obj":obj})
    elif request.method=="POST":
        nid = request.GET.get('nid')
        name = request.POST.get('names')
        models.Teacher.objects.filter(id=nid).update(name=name)
        return redirect("/teacher.html")