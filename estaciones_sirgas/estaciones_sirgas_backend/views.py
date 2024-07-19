from .models import EstacionSirgas
from .serializers import EstacionSirgasSerializador
from rest_framework import generics

# Create your views here.
class EstacionSirgasLista(generics.ListAPIView):
    queryset = EstacionSirgas.objects.all()
    serializer_class = EstacionSirgasSerializador
    name = 'estacion-sirgas-lista'

    