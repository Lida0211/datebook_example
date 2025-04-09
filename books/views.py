from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.template import loader
from books.models import Book
from books.forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def books_main(request):
    books = Book.objects.filter(user=request.user).order_by("upload_date")
    return render(request, "books/books.html", {"books": books})

@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  # Не сохраняем сразу
            book.user = request.user  # Привязываем пользователя
            book.save()  # Теперь сохраняем
            return redirect('books')
    else:
        form = BookForm()
    
    return render(request, 'books/create_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)  # Двойная проверка
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'books/delete_book.html', {'book': book})


