"""xuanke1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app02.views import index,student,teacher,grade,course
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index.index),
    url(r'^teacher.html', teacher.get_teacher),
    url(r'^add_teacher.html', teacher.add_teacher),
    url(r'^delete_teacher.html', teacher.delete_teacher),
    url(r'^edit_teacher.html', teacher.edit_teacher),
    url(r'^student.html',student.student),
    url(r'^add_student.html',student.add_student),
    url(r'^delete_student.html',student.delete_student),
    url(r'^edit_student.html',student.edit_student),
    url(r'^grade.html', grade.grade),
    url(r'^course.html', course.course),

]
