# Generated by Django 5.1.6 on 2025-02-10 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_alter_day_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='activity',
            field=models.CharField(max_length=30, verbose_name='Действие'),
        ),
        migrations.AlterField(
            model_name='day',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='day',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='breakfast',
            field=models.CharField(max_length=30, null=True, verbose_name='Завтрак'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='comment_menu',
            field=models.TextField(null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dinner',
            field=models.CharField(max_length=30, null=True, verbose_name='Ужин'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='lunch',
            field=models.CharField(max_length=30, null=True, verbose_name='Обед'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='snack',
            field=models.CharField(max_length=30, null=True, verbose_name='Перекус'),
        ),
        migrations.AlterField(
            model_name='record',
            name='data',
            field=models.DateField(default=datetime.date(2025, 2, 10), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='record',
            name='weekday',
            field=models.CharField(choices=[('пн', 'понедельник'), ('вт', 'вторник'), ('ср', 'среда'), ('чт', 'четверг'), ('пт', 'пятница'), ('сб', 'суббота'), ('вс', 'воскресенье')], db_default=0, default='mn', max_length=2, verbose_name='День недели'),
        ),
    ]
