from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from music.models import Music
from music.forms import MusicForm



def music_main(request):
    template = loader.get_template("music/music.html")
    music = Music.objects.order_by("upload_date")
    context = {"music":music}
    return HttpResponse(template.render(context, request))

def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music')
    else:
        form = MusicForm()
    
    return render(request, 'music/create_music.html', {'form': form})

def edit_music(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect('music')  
    else:
        form = MusicForm(instance=music)
    
    return render(request, 'music/edit_music.html', {'form': form})


def delete_music(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    
    if request.method == 'POST':
        music.delete()
        return redirect('music')
    
    return render(request, 'music/delete_music.html', {'music': music})