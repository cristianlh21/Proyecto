from django.contrib import admin
from .models import Habitacion, TipoHabitacion

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo_habitacion', 'piso', 'estado')
    list_filter = ('estado', 'tipo_habitacion')
    search_fields = ('numero', 'tipo_habitacion__nombre')
    ordering = ('numero',)

@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    search_fields = ('nombre',)
    ordering = ('nombre',)
