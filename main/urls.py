from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import index_main,col, profil, edit_profil


urlpatterns = [
    path('main/', index_main, name= 'index_main'),
    path('main/calendar/', col),
    path('main/profil/', profil, name = "profil"),
    path('edit/', edit_profil, name = "edit-profil"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
