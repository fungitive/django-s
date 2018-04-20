#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wangj
from django.shortcuts import render,HttpResponse
from app02.models import *
def grade(request):
    return render(request,"grade.html")
