from django import forms
from music.models import Music



class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        exclude = ['user']