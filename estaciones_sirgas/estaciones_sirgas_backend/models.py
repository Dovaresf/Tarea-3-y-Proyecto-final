from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class EstacionSirgas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True)
    monument_type = models.CharField(max_length=100, null=True)
    y_coordinate = models.FloatField(null=True)
    x_coordinate = models.FloatField(null=True)
    installed_on = models.IntegerField(null=True)
    geom = models.PointField()

    def __int__(self): return self.id