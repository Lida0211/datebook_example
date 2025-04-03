from django.contrib import admin
from django.urls import path
from record.views import index, index_id, create_record, edit_record, delete_record


urlpatterns = [
    path('', index, name = 'records'),
    path('<int:record_id>',index_id, name = 'record'),
    path('create/',create_record, name = 'create-record'),
    path('edit/<int:record_id>',edit_record, name = 'edit-record'),
    path('delete/<int:record_id>',delete_record, name = 'delete-record'),
]
