

from django import forms 
from django.forms import ModelForm                
from .models import Socio

class Form_Client(forms.ModelForm):
    
    
    class Meta:
        model= Socio
        fields = "__all__"
        


