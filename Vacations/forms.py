from django import forms
from .models import Vacation

class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ['vacation_desc', 'date_from', 'date_to']