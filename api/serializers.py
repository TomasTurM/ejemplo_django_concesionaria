from rest_framework import serializers
from concesionaria import models

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'car_model',
            'car_brand',
            'year',
            'car_state',
        )
        model = models.Auto