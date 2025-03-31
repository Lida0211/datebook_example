from django.shortcuts import render
from django.urls import path
# Create your views here.

def books_main(request):
    return render(request, "books/books.html")