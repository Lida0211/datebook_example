from django.contrib import admin
from django.urls import path
from record.views import index, index_id, create_record, edit_record, delete_day, create_day, delete_record, create_menu, edit_menu, search_record


urlpatterns = [
    path('', index, name = 'records'),
    path('<int:record_id>',index_id, name = 'record'),
    path('create/',create_record, name = 'create-record'),
    path('createday/',create_day, name = 'create-day'),
    path('edit/<int:day_id>/',edit_record, name = 'edit-record'),
    path('deleteday/<int:day_id>/',delete_day, name = 'delete-day'),
    path('deleterecord/<int:record_id>/',delete_record, name = 'delete-record'),
    path('createmenu/',create_menu, name = 'create-menu'),
    path('editmenu/<int:record_id>/',edit_menu, name = 'edit-menu'),
    path('search/', search_record, name='search_record'),
]
