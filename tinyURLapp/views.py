from django.shortcuts import render, redirect
from django.contrib import messages ## for Flashing Messages

from .models import short_url
from .forms import URLForm
from .shortLogic import Shortner

Shortner_obj = Shortner()

## Home Page
def home(request):

    ## Base URL for Tiny URL's
    BASE_URL = request.get_raw_uri()

    hash_value = ''

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form_details = form.save()
            original_url = form.cleaned_data.get('long_url') ## fetch user provided long URL
            hash_value = Shortner_obj.shorten_url(str(original_url))
            form_details.short_url = hash_value
            form_details.save()

            messages.success(request, f'Long URL converted to following Short URL:\n{BASE_URL}{hash_value}')
            return redirect('tiny-home')
    else:
        form = URLForm()
    
    return render(request, 'tinyURLapp/home.html', {'form': form})

## Redirect Page (i.e. to Original URL Page)
def divert(request, hash_value):
    url_obj = short_url.objects.filter(short_url=hash_value)[0]
    return redirect(url_obj.long_url) 



