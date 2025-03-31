from django.shortcuts import render
from django.urls import path
# Create your views here.

def picture_main(request):
    return render(request, "picture/picture.html")