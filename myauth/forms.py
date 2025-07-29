from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
            'Email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
            }),
        }