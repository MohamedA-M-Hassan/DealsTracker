"""Ejada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from deal_app import views as deal_app_views
from user_app import views as user_app_views
from django.conf.urls import include

urlpatterns = [
    path(r'', user_app_views.index ,name='index',),
    path(r'deal_app/',include('deal_app.urls')),
    path(r'user_app/',include('user_app.urls')),
    path('admin/', admin.site.urls),
    path(r'logout/',user_app_views.user_logout,name='logout'),
    path(r'special/',user_app_views.special,name='special'),

## there is two way to create links
    path(r'sign_up/',user_app_views.sign_up,name='sign_up'),
]
