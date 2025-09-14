from django import forms
from .models import Habitacion, TipoHabitacion

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = ["nombre", "capacidad"]

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'
