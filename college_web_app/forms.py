from django import forms
from .models import *

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['name', 'email', 'contact_no', 'course', 'passing_year', 'company', 'work_address', 'designation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'passing_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'work_address': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
        }

