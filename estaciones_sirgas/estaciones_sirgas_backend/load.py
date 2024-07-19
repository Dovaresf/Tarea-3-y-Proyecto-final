from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import EstacionSirgas

estacionsirgas_mapping = {
    'id': 'id',
    'name': 'name',
    'province': 'province',
    'monument_type': 'monument_type',
    'y_coordinate': 'y_coordinate',
    'x_coordinate': 'x_coordinate',
    'installed_on': 'installed_on',
    'geom': 'POINT',
}

estaciones_sirgas_gpkg = Path(__file__).resolve().parent / 'datos' / 'estaciones_sirgas.gpkg'

def run(verbose=True):
    lm = LayerMapping(EstacionSirgas, estaciones_sirgas_gpkg, estacionsirgas_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)