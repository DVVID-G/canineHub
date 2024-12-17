from rest_framework import viewsets
from .models import Canino
from .serializers import CaninoSerializer
from django.http import HttpResponse
from django.shortcuts import render

class CaninoViewSet(viewsets.ModelViewSet):
    queryset = Canino.objects.all()
    serializer_class = CaninoSerializer

def registro_pedidos(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        canino = request.POST.get("canino")
        # Aquí procesas los datos (guardar en BD, validar, etc.)
        return HttpResponse(f"Pedido registrado para {nombre} - {canino}")
    return render(request, "registro_pedidos.html")
