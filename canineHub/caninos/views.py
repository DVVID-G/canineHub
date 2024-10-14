from django.shortcuts import render
from rest_framework import viewsets
from .models import Canino
from .serializers import CaninoSerializer

class CaninoViewSet(viewsets.ModelViewSet):
    queryset = Canino.objects.all()
    serializer_class = CaninoSerializer
