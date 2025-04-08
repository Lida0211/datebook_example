from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.template import loader
from books.models import Book
from books.forms import BookForm
from django.contrib import messages
# Create your views here.

def books_main(request):
    template = loader.get_template("books/books.html")
    books = Book.objects.order_by("upload_date")
    context = {"books":books}
    return HttpResponse(template.render(context, request))

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    
    return render(request, 'books/create_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'books/delete_book.html', {'book': book})
