from django import forms
from .models import Tarifa, Moneda, ModalidadTarifa, CanalVenta, TipoCambio

class TarifaForm(forms.ModelForm):
    class Meta:
        model = Tarifa
        fields = ["tipo_habitacion", "modalidad", "canal_venta", "moneda", "monto"]

class MonedaForm(forms.ModelForm):
    class Meta:
        model = Moneda
        fields = ["codigo", "nombre"]

class ModalidadForm(forms.ModelForm):
    class Meta:
        model = ModalidadTarifa
        fields = ["nombre"]

class CanalVentaForm(forms.ModelForm):
    class Meta:
        model = CanalVenta
        fields = ["nombre"]

class TipoCambioForm(forms.ModelForm):
    class Meta:
        model = TipoCambio
        fields = ["moneda", "fecha", "valor"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"})
        }
