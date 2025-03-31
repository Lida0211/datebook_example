
from books.views import books_main
from django.urls import path

urlpatterns = [
    path('', books_main),
   
]