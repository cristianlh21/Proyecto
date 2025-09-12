from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva, ReservaHabitacion, HuespedReservaHabitacion
from .forms import ReservaForm, ReservaHabitacionForm, HuespedReservaHabitacionForm

# --- LISTA DE RESERVAS ---
def lista_reservas(request):
    reservas = Reserva.objects.select_related("huesped_reservante").all().order_by("-fecha_ingreso")
    return render(request, "reserva/lista_reservas.html", {"reservas": reservas})

# --- CREAR RESERVA ---
def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect("editar_reserva", pk=reserva.pk)
    else:
        form = ReservaForm()
    return render(request, "reserva/form_reserva.html", {"form": form})

# --- EDITAR RESERVA ---
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("lista_reservas")
    else:
        form = ReservaForm(instance=reserva)
    return render(request, "reserva/form_reserva.html", {"form": form, "reserva": reserva})
