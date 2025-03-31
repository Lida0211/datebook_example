
from picture.views import picture_main
from django.urls import path

urlpatterns = [
    path('', picture_main),
   
]