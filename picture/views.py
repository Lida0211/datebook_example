from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from picture.models import Picture
from picture.forms import PictureForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


@login_required
def picture(request):
    pictures = Picture.objects.filter(user=request.user).order_by("data")
    return render(request, "picture/picture.html", {"pictures": pictures})


@login_required
def create_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user  # Привязываем пользователя
            picture.save()
            return redirect('pictures')
    else:
        form = PictureForm()
    
    return render(request, 'picture/create_picture.html', {'form': form})


@login_required
def edit_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id, user=request.user)  # Фильтр по пользователю
    
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            return redirect('pictures')
    else:
        form = PictureForm(instance=picture)
    
    return render(request, 'picture/edit_picture.html', {'form': form})



@login_required
def delete_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id, user=request.user)
    
    if request.method == 'POST':
        picture.delete()
        return redirect('pictures')
    
    return render(request, 'picture/delete_picture.html', {'picture': picture})