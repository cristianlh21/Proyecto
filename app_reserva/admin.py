from django.contrib import admin
from .models import Reserva, HabitacionReserva, HuespedHabitacionReserva



class HabitacionReservaInline(admin.TabularInline):
    model = HabitacionReserva
    extra = 1
    readonly_fields = ("moneda_original", "monto_ars")


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "reservante", "fecha_ingreso", "fecha_salida", "estado", "monto_total")
    list_filter = ("estado", "fecha_ingreso", "fecha_salida")
    search_fields = ("reservante__apellido", "reservante__nombre", "reservante__documento")
    readonly_fields = ("monto_total",)
    inlines = [HabitacionReservaInline]


class HuespedHabitacionReservaInline(admin.TabularInline):
    model = HuespedHabitacionReserva
    extra = 1


@admin.register(HabitacionReserva)
class HabitacionReservaAdmin(admin.ModelAdmin):
    list_display = ("reserva", "habitacion", "tarifa", "moneda_original", "monto_ars")
    readonly_fields = ("moneda_original", "monto_ars")
    list_filter = ("habitacion", "tarifa__moneda")
    inlines = [HuespedHabitacionReservaInline]
