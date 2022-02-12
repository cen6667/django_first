# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/1/28 11:04 
# @File:urls.py
# @Software:PyCharm

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index_view),
]
