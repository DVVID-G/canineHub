from django.db import models
from pedidos.models import Pedido

class PedidoCanino(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='caninos')
    canino = models.ForeignKey('caninos.Canino', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pedido', 'canino')
