# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/2/5 17:09 
# @File:mymiddleware.py
# @Software:PyCharm
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMW(MiddlewareMixin):

    def process_request(self, request):
        print('MyMW process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW process_view do ---')

    def process_response(self, request, response):
        print('MyMW prcoess_response do ---')
        return response


class MyMW2(MiddlewareMixin):

    def process_request(self, request):
        print('MyMW2 process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW2 process_view do ---')

    def process_response(self, request, response):
        print('MyMW2 prcoess_response do ---')
        return response


class VisitLimie(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):

        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info

        if not re.match('^/test', path_url):
            return

        times = self.visit_times.get(ip_address, 0)
        print('ip', ip_address, '已访问', times)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return
        return HttpResponse('您已经访问过' + str(times) + '次，不能继续访问')
