from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.


def reg_view(request):
    """注册"""
    # GET 返回页面
    if request.method == 'GET':
        return render(request, 'user/register.html')
    # POST 处理提交数据
    elif request.method == 'POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # 1.两次密码一致
        if password_1 != password_2:
            return HttpResponse('两次密码输入不一致')

        # 哈希算法——给定铭文，技术暗处一段定长的，不可逆的值；md5，sha-256
        # 特点
        # 1.定长输出：不管明文多长，哈希都是定长，md5——32位16进制
        # 2.不可逆：无法反向计算 对于的 明文
        # 3.雪崩效应：输入改变，输出必变
        # 场景：1.密码处理 2.文件完整性校验
        # 如何使用
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()

        # 2.用户名是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已经注册')
        # 3.插入数据
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            # 注意并发写入问题——重复插入
            print('--create user error %s' % e)
            return HttpResponse('用户名已注册')
        # 免登录一天
        request.session['username'] = username
        request.session['uid'] = user.id
        # TODO 修改session存储时间为1天

        return HttpResponseRedirect('/index')


def login_view(request):
    if request.method == 'GET':
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        # 检查cookie
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')
    # POST 处理提交数据
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % e)
            return HttpResponse('您的用户名或密码有误')

        # 比对密码
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()

        if password_m != user.password:
            return HttpResponse('您的用户名或密码有误')

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        resp = HttpResponseRedirect('/index')

        # 判断用户是否点选了’记住用户名‘
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)
        # 点选了-》cookie存储 username,uid 时间3天
        return resp
