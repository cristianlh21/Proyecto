from django.db import models

class TipoHabitacion(models.Model):
    """Representa una categoría de habitación del hotel.
       ejemplo: Doble, Doble Matrimonial, Triple, etc.
    Args:
        nombre (str): nombre de la categoría de habitación.
        capacidad (int): capacidad de huéspedes de la habitación.
    """
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveSmallIntegerField()
    
    class Meta:
        verbose_name = "Tipo de Habitación"
        verbose_name_plural = "Tipos de Habitaciones"
        
    def __str__(self):
        return f"{self.nombre} - Capacidad: {self.capacidad}"
    
class Habitacion(models.Model):
    """Representa una habitación física del hotel.
    Args:
        numero (str): número de la habitación.
        tipo_habitacion (TipoHabitacion): tipo de habitación.
        piso (int): piso de la habitación.
        estado (str): estado de la habitación.
    """
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADA', 'Ocupada'),
        ('EN MANTENIMIENTO', 'En mantenimiento'),
        ('RESERVADA', 'Reservada'),
        ('LIMPIEZA', 'Limpieza'),
        ('BAJA', 'Baja'),
        ('SIN USO', 'Sin uso'),
    ]
    numero = models.CharField(max_length=10, unique=True)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, related_name='habitaciones')
    piso = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='DISPONIBLE')
    
    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
    
    def __str__(self):
        return f"{self.numero} - {self.tipo_habitacion} - Piso: {self.piso} - Estado: {self.get_estado_display()}"