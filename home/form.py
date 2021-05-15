from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User




class MyForm(forms.ModelForm):
  
    class Meta:
        model = BlogModel
        fields = ['image']  

 
