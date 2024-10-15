from rest_framework import serializers
from .users import Usuario


# Serializador para los usuarios:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class RoleUserSerializer(serializers.Serializer):
    role = serializers.CharField(allow_null=False, allow_blank=False)

