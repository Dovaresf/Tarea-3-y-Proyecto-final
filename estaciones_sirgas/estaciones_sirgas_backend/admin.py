from django.contrib.gis import admin
from .models import EstacionSirgas

# Register your models here.
# Register your models here.
class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 7,
            'default_lon': -84.0,
            'default_lat': 10.0
        }
    }

@admin.register(EstacionSirgas)
class ObservacionAdmin(CustomGeoAdmin):
    pass