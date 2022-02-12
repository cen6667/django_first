# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/1/24 12:11 
# @File:views.py
# @Software:PyCharm

from django.http import HttpResponse

def page_2003_view(request):
	html = '<h1>这是第一个页面</h1>'
	return HttpResponse(html)

def index_view(request):
	html = '<h1>这是首页</h1>'
	return HttpResponse(html)

def page1_view(request):
	html = '<h1>这是page1</h1>'
	return HttpResponse(html)

def page2_view(request):
	html = '<h1>这是page2</h1>'
	return HttpResponse(html)

def pagen_view(request, pg):
	html = '<h1>这是page %s</h1>' % (pg)
	return HttpResponse(html)

def cal_view(request, n, op, m):
	result = 0
	if op not in ['add', 'sub', 'mul']:
		return HttpResponse('your op is wrong')

	if op == 'add':
		result = n + m
	elif op == 'sub':
		result = n - m
	elif op == 'mul':
		result = n * m
	return HttpResponse('结果为:%s' % result)

def cal2_view(request, x, op, y):
	result = 0
	x = int(x)
	y = int(y)
	if op not in ['add', 'sub', 'mul']:
		return HttpResponse('your op is wrong')

	if op == 'add':
		result = x + y
	elif op == 'sub':
		result = x - y
	elif op == 'mul':
		result = x * y
	return HttpResponse('x:%s %s y:%s结果为:%s' % (x, op, y, result))

def date_view(request, Y, M, D):
	html = '<h1>这是%s年%s月%s日</h1>' % (Y, M, D)
	return HttpResponse(html)





