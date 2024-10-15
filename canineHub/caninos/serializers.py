
from rest_framework import serializers
from .models import Canino

class CaninoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canino
        fields = '__all__'  # Serializa todos los campos del modelo
