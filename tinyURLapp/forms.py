from django import forms
from .models import short_url

## URL Form to provide long URLs
class URLForm(forms.ModelForm):
    class Meta:
        model = short_url ## Model to Interact
        fields = ['long_url'] ## Fields to render/show