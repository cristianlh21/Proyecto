from django import forms
from .models import Reserva, ReservaHabitacion, HuespedReservaHabitacion

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["huesped_reservante", "fecha_ingreso", "fecha_salida", "estado"]
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type": "date"}),
            "fecha_salida": forms.DateInput(attrs={"type": "date"}),
        }

class ReservaHabitacionForm(forms.ModelForm):
    class Meta:
        model = ReservaHabitacion
        fields = ["habitacion", "tarifa", "moneda_original"]

class HuespedReservaHabitacionForm(forms.ModelForm):
    class Meta:
        model = HuespedReservaHabitacion
        fields = ["huesped"]
