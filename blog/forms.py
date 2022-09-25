from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar e-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Modificar nombre')
    last_name = forms.CharField(label='Modificar apellido')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    img = forms.ImageField(label="Imagen")


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['img', 'title', 'subtitle', 'body']
        labels = {
            "img": "Imagen",
            "title": "Título",
            "subtitle": "Subtítulo",
            "body": "Cuerpo",
        }


class PostImgForm(forms.Form):
    img = forms.ImageField(label="Imagen")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'message']
        labels = {
            "user": "Usuario",
            "message": "Mensaje",
        }
