from django.urls import path
from books.views import books_main, create_book, delete_book


urlpatterns = [
    path('', books_main, name ='books'),
    path('create/', create_book, name ='create-book'),
    path('delete/<int:book_id>/', delete_book, name ='delete-book'),
   
]