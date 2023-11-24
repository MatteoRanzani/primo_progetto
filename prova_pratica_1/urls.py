from django.contrib import admin
from django.urls import path,include
from .views import *

app_name="prova_pratica_1"

urlpatterns=[
    path('maxmin', maxmin, name='maxmin'),
    path('media', media, name='media'),
    path('voti', voti, name='voti'),
]