from django.conf import settings
from django.conf.urls.static import static
from picture.views import picture
from django.urls import path

urlpatterns = [
    path('', picture)
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)