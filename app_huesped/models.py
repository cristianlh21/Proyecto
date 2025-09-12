from django.db import models

class Huesped(models.Model):
    ESTADOS = [
        ("RESERVANTE", "Reservante"),
        ("OCUPANTE", "Ocupante"),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="RESERVANTE")

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.estado})"
