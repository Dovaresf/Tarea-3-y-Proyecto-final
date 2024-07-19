from django.urls import path 
from . import views

urlpatterns = [
   path("estacionsirgas/", views.EstacionSirgasLista.as_view(), name=views.EstacionSirgasLista.name) 
]  

