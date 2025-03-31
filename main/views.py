
from django.shortcuts import  render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index_main(request):
    
    return render(request, "main/index_main.html")

def otobr(request):
    return render(request, "registration/login.html")


def col(request):
    return render(request, "main/col.html")

def profil(request):
    return render(request, "main/profil.html")