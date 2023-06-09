# Generated by Django 4.2.1 on 2023-06-02 13:55

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roads',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='roads',
            name='ref',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
