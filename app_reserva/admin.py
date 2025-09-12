from django.contrib import admin
from .models import Reserva, ReservaHabitacion, HuespedReservaHabitacion

# Register your models here.




class HabitacionReservaInline(admin.TabularInline):
    model = ReservaHabitacion
    extra = 1
    readonly_fields = ("moneda_original", "monto_ars")


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_ingreso", "fecha_salida", "estado", "monto_total")



@admin.register(ReservaHabitacion)
class HabitacionReservaAdmin(admin.ModelAdmin):
    list_display = ("reserva", "habitacion", "tarifa", "moneda_original", "monto_ars")
