from django.urls import path
from .views import home, articoloDetailView, lista_articoli_gionalisti

app_name= 'news'

urlpatterns= [
    path("", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", lista_articoli_gionalisti, name="lista_articoli"),
    path("lista_articoli", lista_articoli_gionalisti, name="lista_articoli"),

]