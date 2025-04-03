from django import forms
from record.models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"