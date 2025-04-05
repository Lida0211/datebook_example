from django.db import models
import datetime 



class Picture(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Название')
    data  = models.DateField(null = True,blank=True, default=datetime.date.today(), verbose_name = "Дата")
    image = models.ImageField(upload_to='pictures/', verbose_name='Картинка',blank=False, null=False)
    description = models.TextField(blank=True, null = True, verbose_name = "Описание") 
    
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Картинки"
        verbose_name = "Картинка"
        unique_together = [['name', 'data', 'image']]
