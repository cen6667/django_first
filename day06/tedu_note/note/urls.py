# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/2/3 16:40 
# @File:urls.py
# @Software:PyCharm
from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_note),
]
