# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/1/28 9:57 
# @File:views.py
# @Software:PyCharm
from django.http import HttpResponse
from django.shortcuts import render


def test_static(request):

    return render(request, 'test_static.html')


def set_cookies(request):
    resp = HttpResponse('set cookies is ok')
    resp.set_cookie('uuname', 'cen', 500)
    return resp


def get_cookies(request):
    value = request.COOKIES.get('uuname')

    return HttpResponse('value is %s' % value)


def set_session(request):
    request.session['uname'] = 'wwc'
    return HttpResponse('set session is ok')


def get_session(request):
    value = request.session.get('uname')

    return HttpResponse('session value is %s' % value)
