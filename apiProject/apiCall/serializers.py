from rest_framework import serializers
from . import models

class GridSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'location', 'row', 'col', 'stat')
        model = models.parkingSpace
