# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/2/3 10:38 
# @File:urls.py
# @Software:PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.reg_view),
    path('login', views.login_view),
]
