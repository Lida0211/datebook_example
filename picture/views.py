from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from picture.models import Picture
from picture.forms import PictureForm

from django.contrib import messages

def picture_main(request):
    return render(request, "picture/picture.html")

def picture(request):
    template = loader.get_template("picture/picture.html")
    pictures = Picture.objects.order_by("data")
    context = {"pictures":pictures}
    return HttpResponse(template.render(context, request))


def create_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)  # Важно: request.FILES для изображений
        if form.is_valid():
            form.save()
            return redirect('pictures')  # Перенаправление на список картинок
    else:
        form = PictureForm()
    
    return render(request, 'picture/create_picture.html', {'form': form})


def edit_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            return redirect('pictures')
    else:
        form = PictureForm(instance=picture)
    
    return render(request, 'picture/edit_picture.html', {'form': form})



def delete_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    
    if request.method == 'POST':
        picture.delete()
        return redirect('pictures')
    
    return render(request, 'picture/delete_picture.html', {'picture': picture})