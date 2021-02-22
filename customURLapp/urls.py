from django.urls import path
from . import views

urlpatterns = [
    path('', views.customurl_home, name='custom-home'),
    path('<str:hash_value>/', views.redirect_url, name='redirect-url')
]