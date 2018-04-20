#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wangj
from django.shortcuts import render,HttpResponse,redirect
from app02 import models
def student(request):#显示出全部学生
    student_list=models.Student.objects.all()
    return render(request, "student.html",{"student_list":student_list})
def add_student(request):
    if request.method == "GET":
        grade_list=models.Grade.objects.all()
        return render(request,"add_student.html",{"grade_list":grade_list})
    elif request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        gender=request.POST.get('gender')
        birth=request.POST.get('birth')
        models.Student.objects.create(name=name,
                                      age=age,
                                      gender=gender,
                                      grade_id=grade,
                                      birth=birth)
        return redirect("/student.html")#跳转到url路径
    else :
        return redirect("/add_student.html")

def delete_student(request):
    nid=request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return  redirect("/student.html")
def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Student.objects.filter(id=nid).first()
        grade_list=models.Grade.objects.all()
        return render(request, "edit_student.html", {'obj': obj,'grade_list':grade_list})
    elif request.method == "POST":
        nid=request.GET.get('nid')
        name = request.POST.get('name')
        age = request.POST.get('age')
        class_id = request.POST.get('class_id')
        gender = request.POST.get('gender')
        birth = request.POST.get('birth')
        models.Student.objects.filter(id=nid).update(name=name, age=age,gender=gender,grade_id=class_id,birth=birth)
        return redirect("/student.html")  # 跳转到url路径
    else :
        return (request,"/studnet.html")