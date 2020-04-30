"""djangoshiyan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from hwapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^wuping/', views.wuping),
    url(r'^chaxun/', views.chaxun),
    url(r'^save_users/', views.save_users),
    url(r'^delete1/', views.delete1),
    url(r'^update1/', views.update1),
    url(r'^denglu/', views.denglu),
    url(r'^xunwen/', views.xunwen),
    url(r'^chuxunuser/', views.chuxunuser),
    url(r'^qianduan/', views.qianduan),
    url(r'^qianduandenglu/', views.qianduandenglu),
    url(r'^export_users_csv/', views.export_users_csv),
    url(r'^export_users_xls/', views.export_users_xls),
    url(r'^excel_upload/', views.excel_upload),
    url(r'^excel/', views.excel),
    url(r'^duobiao/', views.duobiao),
]
