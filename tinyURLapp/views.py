from django.shortcuts import render, redirect
from django.contrib import messages ## for Flashing Messages

from .models import short_url
from .forms import URLForm
