"""SocialNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from registrationapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', log_or_reg,name = "log_reg"),
    path('reg_form/', show_reg_form, name = "reg_form"),
    path('reg_success/', show_reg_success, name = "reg_success"),
    path('login/', show_login_form, name = 'login_form'),
    path('welcome/',welcome, name = "welcome"),
    path('logout/',user_logout, name = "logout"),
]
