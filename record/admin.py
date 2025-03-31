from django.contrib import admin

# Register your models here.
from record.models import Record, Day, Menu


admin.site.register(Record)
admin.site.register(Day)
admin.site.register(Menu)