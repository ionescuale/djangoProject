from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Select

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        # fields ='__all__'
        fields = ['first_name', 'last_name', 'course', 'email', 'department', 'active', 'profile']
        #specificam fieldurile dorite in formular

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your last name'}),
            'course': TextInput(attrs={'class':'form-control', 'placeholder': 'Please enter your course'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email'}),
            'department': Select(attrs={'class':'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data #se genereaza un dictionar cu datele completate in formular
        return cleaned_data

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        # fields ='__all__'
        fields = ['first_name', 'last_name', 'course', 'email', 'department', 'active', 'profile']
        #specificam fieldurile dorite in formular

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your last name'}),
            'course': TextInput(attrs={'class':'form-control', 'placeholder': 'Please enter your course'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email'}),
            'department': Select(attrs={'class':'form-select'})
        }