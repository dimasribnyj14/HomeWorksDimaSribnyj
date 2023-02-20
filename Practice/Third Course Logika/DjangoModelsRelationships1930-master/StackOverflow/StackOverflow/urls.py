"""StackOverflow URL Configuration

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
from forum.views import create_question, show_question, show_questions,created_answer

urlpatterns = [
    path('admin/', admin.site.urls),
    path("create_question/",create_question,name='create_question'),
    path("question/Question object (<question_pk>)",show_question,name='question_pk'),
    path("question/",show_questions,name="questions"),
    path("createdanswer/",created_answer,name='created_answer')
]
