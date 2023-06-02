from django.contrib.gis.db import models

# Create your models here.


class Roads(models.Model):
    osm_id = models.BigIntegerField(null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    fclass = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    ref = models.CharField(max_length=250, null=True, blank=True)
    oneway = models.CharField(max_length=250, null=True, blank=True)
    maxspeed = models.IntegerField(null=True, blank=True)
    layer = models.IntegerField(null=True, blank=True)
    bridge = models.CharField(max_length=250, null=True, blank=True)
    tunnel = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk, self.name}"
    
    class Meta:
        managed = False
        db_table = 'roads'

class Building(models.Model):
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}-{self.id}"
    
    class Meta:
        managed = False
        db_table = 'building'