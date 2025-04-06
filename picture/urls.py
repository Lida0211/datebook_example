from django.conf import settings
from django.conf.urls.static import static
from picture.views import picture, create_picture, edit_picture, delete_picture
from django.urls import path

urlpatterns = [
    path('', picture, name='pictures'),
    path('create/', create_picture, name='create-picture'),
    path('edit/<int:picture_id>/', edit_picture, name='edit-picture'),
    path('delete/<int:picture_id>/', delete_picture, name='delete-picture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)