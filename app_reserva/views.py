from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva, ReservaHabitacion, HuespedReservaHabitacion
from .forms import ReservaForm, ReservaHabitacionForm, HuespedReservaHabitacionForm
from app_tarifa_habitacion.models import Tarifa
from app_huesped.models import Huesped

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
            return redirect("editar_reserva_completo", pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, "reserva/form_reserva.html", {"form": form, "reserva": reserva})

# 4️⃣ Editar reserva completo (habitaciones + huéspedes)
def editar_reserva_completo(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    
    # Pre-cargar habitaciones y relaciones necesarias
    habitaciones = reserva.habitaciones.select_related("habitacion", "tarifa", "tarifa__modalidad", "tarifa__canal_venta", "tarifa__moneda").all()

    # Para cada habitación, pre-cargar sus huéspedes
    for hab in habitaciones:
        hab.huespedes_cache = hab.huespedes.select_related("huesped").all()

    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("editar_reserva_completo", pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)

    return render(request, "reserva/editar_reserva_completo.html", {
        "reserva": reserva,
        "form": form,
        "habitaciones": habitaciones,  # ya con huéspedes pre-cargados en hab.huespedes_cache
    })


# --- AGREGAR HABITACIÓN A RESERVA ---
def agregar_habitacion_reserva(request, reserva_pk):
    reserva = get_object_or_404(Reserva, pk=reserva_pk)
    if request.method == "POST":
        form = ReservaHabitacionForm(request.POST)
        if form.is_valid():
            reserva_habitacion = form.save(commit=False)
            reserva_habitacion.reserva = reserva

            # calcular monto_ars según la tarifa y tipo de cambio
            if reserva_habitacion.moneda_original.codigo != "ARS":
                ultimo_tc = reserva_habitacion.moneda_original.tipocambio_set.order_by("-fecha").first()
                if ultimo_tc:
                    reserva_habitacion.monto_ars = reserva_habitacion.tarifa.monto * ultimo_tc.valor
            else:
                reserva_habitacion.monto_ars = reserva_habitacion.tarifa.monto

            reserva_habitacion.save()

            # Cambiar estado de la habitación a RESERVADA
            reserva_habitacion.habitacion.estado = "RESERVADA"
            reserva_habitacion.habitacion.save()

            return redirect("editar_reserva_completo", pk=reserva.pk)
    else:
        form = ReservaHabitacionForm()

    habitaciones_agregadas = reserva.habitaciones.select_related("habitacion", "tarifa").all()
    return render(request, "reserva/form_habitacion_reserva.html", {
        "form": form,
        "reserva": reserva,
        "habitaciones_agregadas": habitaciones_agregadas,
    })
    
def agregar_huesped_habitacion(request, reserva_habitacion_pk):
    reserva_habitacion = get_object_or_404(ReservaHabitacion, pk=reserva_habitacion_pk)
    reserva = reserva_habitacion.reserva

    if request.method == "POST":
        form = HuespedReservaHabitacionForm(request.POST)
        if form.is_valid():
            huesped_rel = form.save(commit=False)
            huesped_rel.reserva_habitacion = reserva_habitacion
            huesped_rel.save()
            return redirect("editar_reserva", pk=reserva.pk)
    else:
        form = HuespedReservaHabitacionForm()

    huespedes_actuales = reserva_habitacion.huespedes.select_related("huesped").all()
    return render(request, "reserva/form_huesped_habitacion.html", {
        "form": form,
        "reserva_habitacion": reserva_habitacion,
        "huespedes_actuales": huespedes_actuales,
    })