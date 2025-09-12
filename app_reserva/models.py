from django.db import models
from app_huesped.models import Huesped
from app_habitacion.models import Habitacion
from app_tarifa_habitacion.models import Tarifa, Moneda

ESTADOS_RESERVA = [
    ("PENDIENTE", "Pendiente"),
    ("CHECKIN", "Check-in"),
    ("CHECKOUT", "Check-out"),
    ("CANCELADA", "Cancelada"),
]

class Reserva(models.Model):
    huesped_reservante = models.ForeignKey(
        Huesped, on_delete=models.PROTECT, related_name="reservas_realizadas",
        blank=True, null=True
    )
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA, default="PENDIENTE")
    monto_total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Reserva #{self.pk} - {self.huesped_reservante} ({self.estado})"
    
class ReservaHabitacion(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="habitaciones")
    habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.PROTECT)
    moneda_original = models.ForeignKey(Moneda, on_delete=models.PROTECT)
    monto_ars = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Reserva #{self.reserva.pk} - Habitación {self.habitacion.numero}"

class HuespedReservaHabitacion(models.Model):
    reserva_habitacion = models.ForeignKey(
        ReservaHabitacion, on_delete=models.CASCADE, related_name="huespedes"
    )
    huesped = models.ForeignKey(Huesped, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.huesped} - Habitación {self.reserva_habitacion.habitacion.numero}"

