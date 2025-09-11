from django.shortcuts import render, get_object_or_404
from .models import Habitacion, TipoHabitacion


def lista_habitaciones(request):
    habitaciones = Habitacion.objects.select_related("tipo_habitacion").all()
    return render(request, "habitacion/lista.html", {"habitaciones": habitaciones})


def detalle_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    return render(request, "habitacion/detalle.html", {"habitacion": habitacion})

from django.shortcuts import render, redirect
from .models import Habitacion, TipoHabitacion
from .forms import HabitacionForm, TipoHabitacionForm

def crear_habitacion(request):
    if request.method == "POST":
        habitacion_form = HabitacionForm(request.POST)
        tipo_form = TipoHabitacionForm(request.POST)

        # Si el usuario quiere crear un tipo nuevo
        tipo = None
        if "crear_tipo" in request.POST and tipo_form.is_valid():
            tipo = tipo_form.save()

        if habitacion_form.is_valid():
            habitacion = habitacion_form.save(commit=False)
            if tipo:
                habitacion.tipo_habitacion = tipo
            habitacion.save()
            return redirect("lista_habitaciones")
    else:
        habitacion_form = HabitacionForm()
        tipo_form = TipoHabitacionForm()

    return render(request, "habitacion/crear_habitacion.html", {
        "habitacion_form": habitacion_form,
        "tipo_form": tipo_form
    })
