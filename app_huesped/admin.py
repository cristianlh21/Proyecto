from django.contrib import admin
from .models import Huesped

@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'pais', 'telefono', 'email', 'estado')
    search_fields = ('nombre', 'apellido', 'documento', 'email')
    list_filter = ('estado', 'pais')
