from django.contrib.gis import admin
from models import Base

admin.site.register(Base, admin.OSMGeoAdmin)
