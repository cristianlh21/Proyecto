from django.db import models
from app_habitacion.models import TipoHabitacion

class CanalVenta(models.Model):
    """Representa un canal de venta de las habitaciones.

    Args:
        nombre (str): Nombre del canal de venta.
        descripción (str): Descripción del canal de venta.

    Returns:
        str: Nombre del canal de venta.
    """
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField( blank=True, null=True)
    
    class Meta:
        verbose_name = "Canal de Venta"
        verbose_name_plural = "Canal de Ventas"
    
    def __str__(self):
        return self.nombre
    
class Moneda(models.Model):
    """Representa una moneda.

    Args:
        código (str): Código de la moneda.
        nombre (str): Nombre de la moneda.
        símbolo (str): Símbolo de la moneda.

    Returns:
        str: Nombre de la moneda.
    """
    
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
    
    def __str__(self):
        return self.nombre
    
class ModalidadTarifa(models.Model):
    """Representa la forma que se calculara la tarifa de la habitación,
    por ejemplo si es por booking, por habitación, por pax, etc.

    Args:
        nombre (str): Nombre de la modalidad de tarifa.

    Returns:
        str: Nombre de la modalidad de tarifa.
    """
    nombre = models.CharField(max_length=50, unique=True, help_text="Ej: Por habitación, Por persona")

    class Meta:
        verbose_name = "Modalidad de tarifa"
        verbose_name_plural = "Modalidades de tarifa"

    def __str__(self):
        return self.nombre


class Tarifa(models.Model):
    """Representa el valor de la habitación.

    Args:
        tipo (TipoHabitacion): Tipo de habitación al que aplica esta tarifa.
        canal_venta (CanalVenta): Canal de venta al que aplica esta tarifa.
        modalidad (ModalidadTarifa): Modalidad de tarifa al que aplica esta tarifa.
        monto (Decimal): Monto de la tarifa.
        moneda (Moneda): Moneda de la tarifa.
        temporada (str): Temporada de la tarifa.

    Returns:
        Tarifa: Tarifa de la habitación.
    """
    tipo = models.ForeignKey(
        TipoHabitacion,
        on_delete=models.CASCADE,
        related_name="tarifas",
        help_text="Tipo de habitación al que aplica esta tarifa"
    )
    canal_venta = models.ForeignKey(CanalVenta, on_delete=models.PROTECT, related_name="tarifas")
    modalidad = models.ForeignKey(ModalidadTarifa, on_delete=models.PROTECT, related_name="tarifas")
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT, related_name="tarifas")
    temporada = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Tarifa"
        verbose_name_plural = "Tarifas"
        unique_together = ('tipo', 'canal_venta', 'modalidad', 'moneda', 'temporada')

    def __str__(self):
        return f"{self.monto} {self.moneda.codigo} ({self.modalidad.nombre})"