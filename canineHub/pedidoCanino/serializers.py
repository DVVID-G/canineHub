from rest_framework import serializers
from .models import PedidoCanino

class PedidoCaninoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCanino
        fields = '__all__'  # Serializa todos los campos del modelo