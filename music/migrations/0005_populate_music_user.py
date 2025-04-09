# Generated by Django 5.1.7 on 2025-04-09 16:46

from django.db import migrations
from django.contrib.auth.models import User

def set_music_user(apps, schema_editor):
    Music = apps.get_model('music', 'Music')
    User = apps.get_model('auth', 'User')
    
    default_user, created = User.objects.get_or_create(
        username='migration_default_user',
        defaults={
            'password': 'unusable_password',
            'is_active': False
        }
    )
    
    Music.objects.filter(user__isnull=True).update(user=default_user)

class Migration(migrations.Migration):
    dependencies = [
        ('music', '0004_music_user'),
    ]
    operations = [migrations.RunPython(set_music_user)]


