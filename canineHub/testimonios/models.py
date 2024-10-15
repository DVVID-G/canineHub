from django.db import models

# testimonios/models.py
from django.db import models
from model_Users.users import Usuario
from pedidos.models import Pedido

class Testimonio(models.Model):
    ESTADO_CHOICES = [
        ('publicado', 'Publicado'),
        ('moderado', 'Moderado'),
        ('eliminado', 'Eliminado'),
    ]

    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='testimonios')
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='testimonios')
    texto = models.TextField()
    multimedia = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonio de {self.id_cliente.nombre} sobre el pedido {self.id_pedido.id}"

