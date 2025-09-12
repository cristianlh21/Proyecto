from django.db import models

class Reserva(models.Model):
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('checkin', 'Check-in'),
        ('checkout', 'Check-out'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    reservante = models.ForeignKey('app_huesped.Huesped', on_delete=models.PROTECT, related_name='reservas')

    def actualizar_monto_total(self):
        total = sum(hr.monto_ars for hr in self.habitaciones_reservadas.all() if hr.monto_ars)
        self.monto_total = total
        self.save()
        
    def __str__(self):
        return f"Reserva {self.id} - {self.reservante}"


class HabitacionReserva(models.Model):
    reserva = models.ForeignKey('app_reserva.Reserva', on_delete=models.CASCADE, related_name='habitaciones_reservadas')
    habitacion = models.ForeignKey('app_habitacion.Habitacion', on_delete=models.PROTECT)
    tarifa = models.ForeignKey('app_tarifa_habitacion.Tarifa', on_delete=models.PROTECT)
    moneda_original = models.ForeignKey('app_tarifa_habitacion.Moneda', on_delete=models.PROTECT)
    monto_ars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Traer datos de la tarifa
        if self.tarifa:
            self.moneda_original = self.tarifa.moneda
            monto_original = self.tarifa.monto

            # Si no es ARS, buscar tipo de cambio
            if self.moneda_original.nombre != "ARS":
                from app_tarifa_habitacion.models import TipoCambio
                tipo_cambio = TipoCambio.objects.filter(
                    moneda=self.moneda_original
                ).order_by('-fecha').first()
                if tipo_cambio:
                    self.monto_ars = monto_original * tipo_cambio.valor
            else:
                self.monto_ars = monto_original

        super().save(*args, **kwargs)
        self.reserva.actualizar_monto_total()
    def __str__(self):
        return f"Habitación {self.habitacion} en Reserva {self.reserva}"
    
class HuespedHabitacionReserva(models.Model):
    habitacion_reserva = models.ForeignKey('app_reserva.HabitacionReserva', on_delete=models.CASCADE, related_name='huespedes')
    huesped = models.ForeignKey('app_huesped.Huesped', on_delete=models.PROTECT)

    def __str__(self):
        return f"Huesped {self.huesped} en Habitación {self.habitacion_reserva}"