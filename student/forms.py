from django import forms
from django.forms import TextInput, NumberInput, EmailInput, DateInput, Select, Textarea

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields ='__all__'
        fields = ['first_name', 'last_name', 'age', 'email', 'description', 'active', 'start_date', 'end_date',
                  'gender', 'trainer', 'profile']
        #specificam fieldurile dorite in formular

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your last name'}),
            'age': NumberInput(attrs={'class':'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email'}),
            'description': Textarea(attrs={'class':'form-control', 'placeholder':'Please enter your description', 'rows':3}),
            'start_date': DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': DateInput(attrs={'class':'form-control', 'type':'date'}),
            'gender': Select(attrs={'class':'form-select'}),
            'trainer': Select(attrs={'class':'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data #se genereaza un dictionar cu datele completate in formular

        #o unicitate pt adresa de mail
        get_email = cleaned_data.get('email')  # cleaned_data['email']
        checks_email = Student.objects.filter(email=get_email)
        if checks_email:
            msg = 'This email address already exists'
            self._errors['email'] = self.error_class([msg]) #afisez pe fieldul email eroarea din variabila msg

        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date > end_date:
            msg = 'Start date should be less than end date'
            self._errors['start_date'] = self.error_class([msg])  # afisez pe fieldul email eroarea din variabila msg


        return cleaned_data

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'description', 'active', 'start_date', 'end_date',
                  'gender', 'trainer', 'profile']
        #specificam fieldurile dorite in formular

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your last name'}),
            'age': NumberInput(attrs={'class':'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email'}),
            'description': Textarea(attrs={'class':'form-control', 'placeholder':'Please enter your description', 'rows':3}),
            'start_date': DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': DateInput(attrs={'class':'form-control', 'type':'date'}),
            'gender': Select(attrs={'class':'form-select'}),
            'trainer': Select(attrs={'class':'form-select'}),
        }


# Class Meta intr-un proiect Django  este folosit pentru
# a defini metadatele asociate cu un formular

# Aceste metadate includ informatii despre modelul (Student)
# legat de formularul, campurile care trebuiesc sa apara in formular
# si pe care le putem customiza, adaugand clase de CSS, placeholder etc.