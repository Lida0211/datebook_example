from django.contrib import admin
from django.urls import path
from main.views import index_main, otobr, col, profil, edit_profil


urlpatterns = [
    path('', otobr, name = "login"),
    path('main/', index_main),
    path('main/calendar/', col),
    path('main/profil/', profil, name = "profil"),
    path('edit/', edit_profil, name = "edit-profil"),
]
