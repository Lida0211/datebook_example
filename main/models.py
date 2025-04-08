from django.db import models

# Create your models here.

class PersonalData(models.Model):
    foto = models.ImageField(upload_to='pictures/', verbose_name='Фото',blank=False, null=False)
    surname = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Фамилия")
    name = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Имя")
    patronymic = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Отчество")
    phone = models.CharField( max_length=20,verbose_name="Номер телефона",help_text="В формате +375XXXXXXXXX или 80XXXXXXXXX",blank=True,)
    email = models.EmailField(verbose_name="Электронная почта",max_length=255, unique=True, help_text="Введите действительный email адрес",blank=True,null=True) 
    address = models.TextField(blank=True, null = True, verbose_name = "Адрес") 
    hobby = models.TextField(blank=True, null = True, verbose_name = "Хобби")
    
    class Meta:
        verbose_name_plural = "Профиль"
        verbose_name = "Профиль"
        
    
    def __str__(self):
        return f"{self.surname} - {self.name}"