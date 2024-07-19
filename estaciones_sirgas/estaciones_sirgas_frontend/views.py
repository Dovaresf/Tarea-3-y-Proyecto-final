from django.shortcuts import render

# Create your views here.
def estacionessirgasListaMapa(request):
    return render(request, 'estaciones_sirgas_frontend/estaciones_sirgas_base.html')