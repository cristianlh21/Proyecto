# app_tarifa_habitacion/models.py
from django.db import models
from app_habitacion.models import TipoHabitacion

class Moneda(models.Model):
    codigo = models.CharField(max_length=10, unique=True)  # Ej: USD, ARS
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo

class ModalidadTarifa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # Particular, Agencia, etc.

    def __str__(self):
        return self.nombre

class Canal(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # Booking, Despegar, Directo

    def __str__(self):
        return self.nombre

class TipoCambio(models.Model):
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # 1 unidad de moneda = ? ARS

    class Meta:
        unique_together = ("moneda", "fecha")

    def __str__(self):
        return f"{self.moneda.codigo} - {self.fecha} = {self.valor} ARS"

class Tarifa(models.Model):
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    modalidad = models.ForeignKey(ModalidadTarifa, on_delete=models.CASCADE)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # precio en moneda original
    monto_ars = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Buscar último tipo de cambio de la moneda
        if self.moneda.codigo != "ARS":
            ultimo_tc = TipoCambio.objects.filter(moneda=self.moneda).order_by("-fecha").first()
            if ultimo_tc:
                self.monto_ars = self.monto * ultimo_tc.valor
        else:
            self.monto_ars = self.monto
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_habitacion} | {self.modalidad} | {self.canal} | {self.monto} {self.moneda.codigo}"
