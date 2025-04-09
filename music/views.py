from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from music.models import Music
from music.forms import MusicForm
from django.contrib.auth.decorators import login_required



@login_required
def music_main(request):
    music = Music.objects.filter(user=request.user).order_by("upload_date")
    return render(request, "music/music.html", {"music": music})

@login_required
def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user  # Привязываем текущего пользователя
            music.save()
            return redirect('music')
    else:
        form = MusicForm()
    
    return render(request, 'music/create_music.html', {'form': form})

@login_required
def edit_music(request, music_id):
    music = get_object_or_404(Music, id=music_id, user=request.user)  # Фильтр по пользователю
    
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect('music')
    else:
        form = MusicForm(instance=music)
    
    return render(request, 'music/edit_music.html', {'form': form})


@login_required
def delete_music(request, music_id):
    music = get_object_or_404(Music, pk=music_id, user=request.user)  # Фильтр по пользователю
    
    if request.method == 'POST':
        music.delete()
        return redirect('music')
    
    return render(request, 'music/delete_music.html', {'music': music})