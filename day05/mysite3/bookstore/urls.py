# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/2/1 15:53 
# @File:urls.py
# @Software:PyCharm

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all_book', views.all_book),
    path('update_book/<int:book_id>', views.update_book),
    # http://127.0.0.1:8000/bookstore/delete?book_id=xx
    path('delete_book', views.delete_book),

]
