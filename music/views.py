from django.shortcuts import render

# Create your views here.
def music_main(request):
    return render(request, "music/music.html")