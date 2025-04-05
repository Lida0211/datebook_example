from django.db import models
import datetime
# Create your models here.


class Record(models.Model):
    week_day = (
        ("пн", "понедельник"),
        ("вт","вторник"),
        ("ср","среда"),
        ("чт","четверг"),
        ("пт","пятница"), 
        ("сб","суббота"),
        ("вс","воскресенье"),
    )
    data  = models.DateField(null = False, default=datetime.date.today(), verbose_name = "Дата")                             #дата
    weekday = models.CharField(max_length = 2, null = False, default="пн", verbose_name = "День недели", choices=week_day, db_default=0)             #день недели
      
    def __str__(self):
        return str(self.data)


    class Meta:
        verbose_name_plural = "Записи"
        verbose_name = "Запись"
        ordering = ["-data"]

class Day(models.Model):
    time = models.TimeField(null = False, verbose_name = "Время")                         #время
    activity = models.CharField(max_length = 30, null = False, verbose_name = "Действие")      #действие
    comment = models.TextField(blank=True, null = True, verbose_name = "Комментарий")                      #комментарий
    record = models.ForeignKey(Record, on_delete=models.CASCADE,verbose_name = "Запись", default=1, related_name="days")



    class Meta:
        verbose_name_plural = "Распорядок дня"
        verbose_name = "Распорядок дня"
        ordering = ["time"]
        unique_together = [['time', 'record']]

class Menu(models.Model):
    breakfast = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Завтрак")      #завтрак
    lunch = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Обед")          #обед
    dinner = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Ужин")         #ужин
    snack = models.CharField(blank=True, max_length = 30, null = True, verbose_name = "Перекус")          #перекус
    comment_menu = models.TextField(blank=True, null = True, verbose_name = "Примечание")                  #примечания к меню
    record = models.ForeignKey(Record, on_delete=models.CASCADE,verbose_name = "Запись", default=1, related_name="menu")


    class Meta:
        verbose_name_plural = "Меню"
        verbose_name = "Меню"
        constraints = [
            models.UniqueConstraint(
                fields=['record'],
                name='unique_menu_per_record',
                violation_error_message='Меню уже существует для этой записи'
            )
        ]
        






        


                        