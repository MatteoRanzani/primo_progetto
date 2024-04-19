from django.urls import path
from .views import *

app_name= 'news'

urlpatterns= [
    path("", home, name="homeview"),
    path("articoli", articoloDetailView, name="articolo_detail"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", lista_articoli_giornalisti, name="lista_articoli"),
    path("lista_articoli/", lista_articoli_giornalisti, name="lista_articoli"),
    path("homepage_news/", home, name="homepage_news"),
    path("query/", query_base, name="query"),
    path("gionalisti/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("lista_giornalisti/", lista_giornalisti, name="lista_giornalisti"),
    path('index_news/', index_news, name="index_news"),
    path("giornalisti_list_api/", giornalisti_list_api, name="giornalisti_list_api"),
    path("giornalista_api/<int:pk>",giornalista_api, name="giornalista_api"),
]