from django import forms
from .models import *



class MyForm(forms.ModelForm):
  
    class Meta:
        model = BlogModel
        fields = ['image']        