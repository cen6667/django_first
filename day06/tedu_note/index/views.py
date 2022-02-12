from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def index_view(request):
    return render(request, 'index/index.html')


def delete_remember(request):
    # 删除cookies
    response = HttpResponseRedirect('/index')
    response.delete_cookie('username')
    response.delete_cookie('password')
    # 删除session
    request.session.flush()
    return response
