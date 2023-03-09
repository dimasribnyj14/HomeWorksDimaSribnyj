from django.shortcuts import render

# Create your views here.
def oof(request):
    return render(request, 'index.html')