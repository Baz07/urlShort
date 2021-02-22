from django import forms
from .models import short_url

class URLForm(forms.ModelForm):
    class Meta:
        model = short_url
        fields = ['long_url']