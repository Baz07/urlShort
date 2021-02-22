from django.urls import path
from . import views


urlpatterns = [
    ## API for Home View
    path('', views.home, name='tiny-home'),

    ## API for Divert View
    path('<str:hash_value>', views.divert, name='tiny-divert'),

]