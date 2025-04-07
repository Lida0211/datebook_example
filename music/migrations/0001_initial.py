# Generated by Django 5.1.7 on 2025-04-07 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, default=datetime.date(2025, 4, 7), null=True, verbose_name='Дата')),
                ('title', models.CharField(max_length=100, verbose_name='Название трека')),
                ('artist', models.CharField(max_length=100, verbose_name='Исполнитель')),
                ('audio_file', models.FileField(upload_to='music/', verbose_name='Аудиофайл')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='Длительность')),
                ('description', models.TextField(blank=True, verbose_name='Описание трека')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
            options={
                'verbose_name': 'Музыкальный трек',
                'verbose_name_plural': 'Музыкальные треки',
            },
        ),
    ]
