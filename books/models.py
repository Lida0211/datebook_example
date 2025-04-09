from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length = 30, null = False, verbose_name = "Название")
    author = models.TextField(blank=True, null = True, verbose_name = "Автор")
    description= models.TextField(blank=True, null = True, verbose_name = "Описание")
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    
    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        
    
    def __str__(self):
        return f"{self.name} - {self.author}"