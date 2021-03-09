"""rajivdahal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('',views.index,name='index'),
    path('post',views.post,name='post'),
    path('blogs',views.blogs,name='blogs'),
    path('more',views.more,name='blogs'),
    path('viewpost/<slug:slug_text>/',views.viewpost,name='viewpost'),
    path('viewblog/<slug:slug_text>/',views.viewblog,name='viewblog'),
    path('trendingpost/<slug:slug_text>/',views.trendingpost,name='trendingposts'),
]


