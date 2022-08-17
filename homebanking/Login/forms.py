from dataclasses import field, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm




class UserRegistrationForm(UserCreationForm,ModelForm):
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    dni = forms.CharField(label="DNI", max_length=8)

    class Meta:
        model=User
        fields = ['username', 'email', 'first_name', 'dni']
        #help_texts= {k:"" for k in fields}

