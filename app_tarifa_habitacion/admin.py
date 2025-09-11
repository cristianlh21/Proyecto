from django.contrib import admin
from .models import CanalVenta, Moneda, ModalidadTarifa, Tarifa

@admin.register(CanalVenta)
class CanalVentaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')


@admin.register(ModalidadTarifa)
class ModalidadTarifaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'canal_venta', 'modalidad', 'monto', 'moneda', 'temporada')
    list_filter = ('tipo', 'canal_venta', 'modalidad', 'moneda', 'temporada')
    search_fields = ('tipo__nombre', 'canal_venta__nombre', 'modalidad__nombre')
