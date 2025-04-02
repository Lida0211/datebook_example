from django.contrib import admin
from django.urls import path
from record.views import index, index_id


urlpatterns = [
    path('', index, name = 'records'),
    path('<int:record_id>',index_id, name = 'record'),
]
