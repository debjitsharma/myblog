from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class MyForm(forms.ModelForm):
  
    class Meta:
        model = BlogModel
        fields = ['image']  

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']  
