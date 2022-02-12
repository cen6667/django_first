# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/1/28 9:57 
# @File:views.py
# @Software:PyCharm

from django.shortcuts import render


def test_static(request):

    return render(request, 'test_static.html')


