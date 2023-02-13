"""OnlineShop URL Configuration

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
from OnlineShopApp.views import *
from ForumApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', show_reg_form, name='reg_form'),
    path('reg_success', show_reg_success, name='reg_success'),
    path('login_form', show_login_form, name = 'login_form'),
    path('welcome', welcome, name='welcome'),
    path('forum',show_forum,name='forum'),
    path('product',show_product,name='product'),
]
from OnlineShop.settings import MEDIA_ROOT, MEDIA_URL, DEBUG
from django.conf.urls.static import static
if DEBUG:
	urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
