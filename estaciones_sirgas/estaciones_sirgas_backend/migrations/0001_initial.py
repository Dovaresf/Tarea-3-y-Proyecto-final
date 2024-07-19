# Generated by Django 4.2.14 on 2024-07-19 03:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstacionSirgas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('province', models.CharField(max_length=20, null=True)),
                ('monument_type', models.CharField(max_length=20, null=True)),
                ('y_coordinate', models.FloatField(null=True)),
                ('x_coordinate', models.FloatField(null=True)),
                ('installed_on', models.IntegerField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
