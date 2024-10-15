from django.db import models
from model_Users.users import Usuario

class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES = [
        ('procesado', 'Procesado'),
        ('pendiente', 'Pendiente'),
        ('cancelado', 'Cancelado'),
    ]

    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDO_CHOICES)
    metodo_pago = models.CharField(max_length=255)
    comprobante_pago = models.TextField(blank=True, null=True)
    direccion_envio = models.CharField(max_length=255)
    direccion_facturacion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.estado_pedido}"

