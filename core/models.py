from django.contrib.gis.db import models

# Create your models here.
class Buildings(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'buildings'

class Landuse(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'landuse'

class Natrual(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'natrual'

class Places(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    population = models.CharField(max_length=250)
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'places'

class Pofw(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'pofw'

class Railway(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    layer = models.CharField(max_length=250)
    bridge = models.CharField(max_length=250)
    tunnel = models.CharField(max_length=250)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'railways'

class Roads(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
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

class Traffic(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.PointField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'traffic'

class Transport(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.PointField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'transport'



class Water(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'water'


class Waterways(models.Model):
    id = models.AutoField(primary_key=True, name='gid')
    osm_id = models.BigIntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'waterways'


