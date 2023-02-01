from django.shortcuts import render
from django.http import StreamingHttpResponse
from WSGIREF.UTIL import FIleWrapper
import nimetypes
def show_dark(request):
    return render(request,'index.html')