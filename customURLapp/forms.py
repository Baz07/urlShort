from django import forms
from .models import custom_url

class CustomURLForm(forms.ModelForm):
    class Meta:
        model = custom_url
        fields = '__all__'  