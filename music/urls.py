from music.views import music_main
from django.urls import path

urlpatterns = [
    path('', music_main),
   
]