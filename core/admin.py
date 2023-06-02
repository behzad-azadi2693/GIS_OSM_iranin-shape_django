from django.contrib import admin
from leaflet.admin import LeafletGeoAdminMixin

# Register your models here.
from .models import Roads, Building

class RoadsAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

class BuildingAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    ordering = ('-geom', )

admin.site.register(Roads, RoadsAdmin)
admin.site.register(Building, BuildingAdmin)