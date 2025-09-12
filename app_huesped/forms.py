from django import forms
from .models import Huesped

class HuespedForm(forms.ModelForm):
    class Meta:
        model = Huesped
        fields = ["nombre", "apellido", "numero_documento", "direccion", "pais", "telefono", "email", "estado"]
