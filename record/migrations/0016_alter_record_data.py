# Generated by Django 5.1.7 on 2025-04-09 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0015_alter_record_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='data',
            field=models.DateField(default=datetime.date(2025, 4, 9), verbose_name='Дата'),
        ),
    ]
