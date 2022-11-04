from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    passwordAgain = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'passwordAgain'
        ]
