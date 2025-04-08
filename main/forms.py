from django import forms
from main.models import PersonalData

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = "__all__"