from django import forms
from django.forms import TextInput, EmailInput, Textarea, Select

from feedback.models import Feedback



class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback

        fields = ['first_name', 'last_name', 'email', 'trainer', 'message', 'active']

        widgets ={
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'trainer': Select(attrs={'class': 'form-control'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your feedback'}),
        }


class FeedbackUpdateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'trainer', 'message', 'active']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'trainer': Select(attrs={'class': 'form-control'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your feedback'}),
        }