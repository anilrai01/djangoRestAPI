from django.contrib import admin
from . models import location
from . models import parkingSpace

# Register your models here.

admin.site.register(location)
admin.site.register(parkingSpace)
