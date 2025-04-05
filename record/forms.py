from django import forms
from record.models import Record, Day, Menu

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = "__all__"

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"