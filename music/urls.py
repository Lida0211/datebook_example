from django.conf import settings
from django.conf.urls.static import static
from music.views import music_main, create_music, delete_music, edit_music
from django.urls import path

urlpatterns = [
    path('', music_main, name = 'music'),
    path('create/', create_music, name = 'create-music'),
    path('delete/<int:music_id>/', delete_music, name = 'delete-music'),
    path('edit/<int:music_id>/', edit_music, name = 'edit-music'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)