# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/1/28 11:12 
# @File:urls.py
# @Software:PyCharm

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/sport/index
    path('index', views.index_view),
]