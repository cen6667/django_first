"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

# 按顺序匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/page/2003/
    path('page/2003/', views.page_2003_view),
    # http://127.0.0.1:8000/
    path('', views.index_view),
    # http://127.0.0.1:8000/page/1/
    path('page/1', views.page1_view),
    # http://127.0.0.1:8000/page/2/
    path('page/2', views.page2_view),
    # http://127.0.0.1:8000/page/3-100
    path('page/<int:pg>', views.pagen_view),
    # http://127.0.0.1:8000/整数/操作符/整数
    # 正则re_path
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),
    # # http://127.0.0.1:8000/整数/操作符/整数
    # path('<int:n>/<str:op>/<int:m>', views.cal_view),
    # http://127.0.0.1:8000/年4/月2/日2
    re_path(r'^(?P<Y>\d{4})/(?P<M>\d{2})/(?P<D>\d{2})$', views.date_view),
]
