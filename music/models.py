from django.db import models
import datetime 


class Music(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название трека")
    artist = models.CharField(max_length=100, verbose_name="Исполнитель")
    audio_file = models.FileField(upload_to='music/', verbose_name="Аудиофайл")
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    
    class Meta:
        verbose_name_plural = "Музыкальные треки"
        verbose_name = "Музыкальный трек"
        
    
    def __str__(self):
        return f"{self.title} - {self.artist}"