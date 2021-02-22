from django import forms
from .models import custom_url

## Form for Users to add Long URL and Short/Hash Value
class CustomURLForm(forms.ModelForm):
    class Meta:
        model = custom_url
        fields = '__all__'  