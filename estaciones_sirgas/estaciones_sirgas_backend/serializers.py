from .models import EstacionSirgas
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class EstacionSirgasSerializador(GeoFeatureModelSerializer):
    class Meta:
        model = EstacionSirgas
        geo_field = 'geom'

        fields = (
            'id',
            'name',
            'province',
            'monument_type',
            'y_coordinate',
            'x_coordinate',
            'installed_on'
        )

