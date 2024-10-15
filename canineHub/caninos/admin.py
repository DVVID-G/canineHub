

# Register your models here.
# caninos/admin.py
from django.contrib import admin
from .models import Canino

@admin.register(Canino)
class CaninoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'tamaño', 'precio', 'disponibilidad', 'fecha_creacion')
