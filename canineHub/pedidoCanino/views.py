from django.shortcuts import render
from rest_framework import viewsets
from .models import PedidoCanino
from .serializers import PedidoCaninoSerializer

class PedidoCaninoViewSet(viewsets.ModelViewSet):
    queryset = PedidoCanino.objects.all()
    serializer_class = PedidoCaninoSerializer


# Create your views here.
