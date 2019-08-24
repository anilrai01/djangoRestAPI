from django.db import models

# Create your models here.

class location(models.Model):
    """Defines the Location of the Parking Space"""
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class parkingSpace(models.Model):
    """Defines the parking location and seats"""
    location = models.ForeignKey(location, on_delete = models.CASCADE)
    row = models.IntegerField()
    col = models.IntegerField()
    stat = models.BooleanField(default = False)
