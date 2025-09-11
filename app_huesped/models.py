
from django.db import models

class Huesped(models.Model):
    ESTADO_CHOICES = [
        ('reservante', 'Reservante'),
        ('ocupante', 'Ocupante'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='reservante')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
