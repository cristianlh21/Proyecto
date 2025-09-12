from django.shortcuts import render, get_object_or_404
from .models import Habitacion, TipoHabitacion


# views.py
from django.shortcuts import render
from .models import Habitacion

def lista_habitaciones(request):
    estado = request.GET.get("estado")
    queryset = Habitacion.objects.exclude(estado="BAJA")  # no mostramos eliminadas

    if estado:
        queryset = queryset.filter(estado=estado)

    habitaciones = queryset.select_related("tipo_habitacion")
    return render(request, "habitacion/lista.html", {
        "habitaciones": habitaciones,
        "estado": estado,
    })




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


def editar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect("lista_habitaciones")
    else:
        form = HabitacionForm(instance=habitacion)

    return render(request, "habitacion/editar_habitacion.html", {"form": form, "habitacion": habitacion})

def editar_tipo_habitacion(request, pk):
    tipo = get_object_or_404(TipoHabitacion, pk=pk)
    if request.method == "POST":
        form = TipoHabitacionForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect("lista_habitaciones")
    else:
        form = TipoHabitacionForm(instance=tipo)

    return render(request, "habitacion/editar_tipo_habitacion.html", {"form": form, "tipo": tipo})

def eliminar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    habitacion.estado = "BAJA"   # eliminación virtual
    habitacion.save()
    return redirect("lista_habitaciones")

def lista_tipo_habitacion(request):
    tipos = TipoHabitacion.objects.all()
    return render(request, "habitacion/lista_tipo_habitacion.html", {"tipos": tipos})

def crear_tipo_habitacion(request):
    if request.method == "POST":
        tipo_form = TipoHabitacionForm(request.POST)
        if tipo_form.is_valid():
            tipo_form.save()
            return redirect("lista_habitaciones")
    else:
        tipo_form = TipoHabitacionForm()
    return render(request, "habitacion/crear_tipo_habitacion.html", {"tipo_form": tipo_form})

def editar_tipo_habitacion(request, pk):
    tipo = get_object_or_404(TipoHabitacion, pk=pk)
    if request.method == "POST":
        form = TipoHabitacionForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect("lista_habitaciones")
    else:
        form = TipoHabitacionForm(instance=tipo)

    return render(request, "habitacion/editar_tipo_habitacion.html", {"form": form, "tipo": tipo})

def eliminar_tipo_habitacion(request, pk):
    tipo = get_object_or_404(TipoHabitacion, pk=pk)
    tipo.delete()
    return redirect("lista_habitaciones")