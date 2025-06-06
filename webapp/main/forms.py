from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Avatar


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['avatar']
    avatar = forms.ImageField(required=True)