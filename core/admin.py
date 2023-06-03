from django.contrib import admin
from leaflet.admin import LeafletGeoAdminMixin

# Register your models here.
from .models import ( 
    Buildings, Landuse, Natrual, Places, Pofw, Railway, 
    Roads, Traffic, Transport, Water, Waterways
    )


class BuildingAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class LanduseAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class NatrualAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class PlacesAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class PofwAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class RailwayAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class TrafficAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class TransportAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class WaterAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class WaterwaysAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class RoadsAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

admin.site.register(Roads, RoadsAdmin)
admin.site.register(Buildings, BuildingAdmin)
admin.site.register(Landuse, LanduseAdmin)
admin.site.register(Natrual, NatrualAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Pofw, PofwAdmin)
admin.site.register(Railway, RailwayAdmin)
admin.site.register(Traffic, TrafficAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Water, WaterAdmin)
admin.site.register(Waterways, WaterwaysAdmin)
