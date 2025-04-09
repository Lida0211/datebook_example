from django import forms
from record.models import Record, Day, Menu

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['user']

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        exclude = ['user']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ['user']