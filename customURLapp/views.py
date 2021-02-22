from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import custom_url
from .forms import CustomURLForm


#####################################
### Custom URL Generation ###########
#####################################

## Home Page
def customurl_home(request):

    BASE_URL = request.get_raw_uri()

    if request.method == 'POST':
        form = CustomURLForm(request.POST)
        if form.is_valid():
            form_details = form.save()
            hash_value = form.cleaned_data.get('hash_value') ## Fetch the User provided hash value
            form_details.custom_url = hash_value
            form_details.save()

            messages.success(request, f'Your Short URL: {BASE_URL}{hash_value}')

            return redirect('custom-home')
    else:
        form  = CustomURLForm()

    return render(request, 'customURLapp/custom.html', {'form': form})

## For Redirecting the short custom URL to Original URL
def redirect_url(request, hash_value):
    url_obj = custom_url.objects.filter(hash_value=hash_value)
    if url_obj:
        url_obj = url_obj[0]
        return redirect(url_obj.original_url)
    else:
        return render(request, 'customURLapp/404.html')
