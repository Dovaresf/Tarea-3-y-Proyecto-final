from django.urls import path
from . import views

app_name = 'estaciones_sirgas_frontend'
urlpatterns = [
    path('', views.estacionessirgasListaMapa, name='estacionessirgas-lista-mapa')
]

