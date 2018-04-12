#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wangj
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'showtime/',views.showtime),
    url(r'^article/(\d{4})$', views.article_year),
    url(r'^article/(?P<years>\d{4})/(?P<months>\d{2})', views.article_years),
    url(r'^registry/', views.registry,name="reg"),
]