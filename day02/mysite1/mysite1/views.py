# @Author: zyc
# -*- coding: utf-8 -*-
# @Time: 2022/1/24 12:11 
# @File:views.py
# @Software:PyCharm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

POST_FORM = """
<form method='post' action='/test_get_post'>
	用户名：<input type='test' name='uname'>
	<input type='submit' value='提交'>
</form>
"""


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


def test_request(request):
    print('path info is', request.path_info)
    print('method is', request.method)
    print('querystring is', request.GET)
    print('full path is', request.get_full_path())
    print('META[REMOTE_ADDR] is', request.META['REMOTE_ADDR'])

    # return HttpResponse('test request ok')
    # 302跳转
    return HttpResponseRedirect('/page/1')


def test_get_post(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.GET['a'])
        print(request.GET.get('c', 'no c'))
        print(request.GET.getlist('a'))
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        print('uname is', request.POST['uname'])
        return HttpResponse('post is ok')
        pass
    else:
        pass

    return HttpResponse('--test get post is ok--')


def test_html(request):
    # 方案一
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    # 方案二
    from django.shortcuts import render
    dic = {'username': 'zyc', 'age': 24}
    return render(request, 'test_html.html', dic)


def test_html_param(request):
    dic = {}
    dic['int'] = 88
    dic['str'] = 'zhangsan'
    dic['lst'] = ['Tom', 'Jack', 'Lily']
    dic['dict'] = {'a': 9, 'b': 8}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(11111)</script>'

    return render(request, 'test_html_param.html', dic)


def say_hi():
    return 'hahha'


class Dog:
    def say(self):
        return 'wangwang'


def test_if_for(request):
    dic = {}
    dic['x'] = 10
    dic['lst'] = ['TOM', 'Jack', 'Lily']
    return render(request,'test_if_for.html', dic)


def test_mycal(request):

    if request.method == 'GET':
        return render(request, 'test_mycal.html')
    elif request.method == 'POST':
        # 处理计算
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        if op == 'add':
            result = x+y
        elif op == 'sub':
            result = x-y
        elif op == 'mul':
            result = x*y
        elif op == 'div':
            result = x/y

        # locals 可以帮助我们自动将上面的参数生成字典
        return render(request, 'test_mycal.html', locals())

def base_view(request):
    lst = ['zhansan','wangwu']
    return render(request, 'base.html',locals())



def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')

def test_url(request):

    return render(request, 'test_url.html')


def test_url_result(request, age):
    # 302跳转
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)

    # return HttpResponse('test url is ok')
