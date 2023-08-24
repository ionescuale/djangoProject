from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter password'})


class UserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['last_name', 'first_name', 'email'
                  # , 'username'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs.update(
        #     {'class': 'form-control', 'placeholder': 'Please enter username'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter last name'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter first name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter email'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please reenter password'})


