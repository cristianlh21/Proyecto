from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarifa, TipoCambio
from .forms import TarifaForm, MonedaForm, ModalidadForm, CanalVentaForm, TipoCambioForm


# Listar todas las tarifas
def lista_tarifas(request):
    tarifas = Tarifa.objects.select_related(
        "tipo_habitacion", "modalidad", "canal_venta", "moneda"
    )
    return render(request, "tarifas/lista_tarifas.html", {"tarifas": tarifas})

# Crear una tarifa
def crear_tarifa(request):
    if request.method == "POST":
        form = TarifaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tarifas")
    else:
        form = TarifaForm()
    return render(request, "tarifas/form_tarifa.html", {"form": form})

# Editar una tarifa
def editar_tarifa(request, pk):
    tarifa = get_object_or_404(Tarifa, pk=pk)
    if request.method == "POST":
        form = TarifaForm(request.POST, instance=tarifa)
        if form.is_valid():
            form.save()
            return redirect("lista_tarifas")
    else:
        form = TarifaForm(instance=tarifa)
    return render(request, "tarifas/form_tarifa.html", {"form": form})

# Eliminar una tarifa (física)
def eliminar_tarifa(request, pk):
    tarifa = get_object_or_404(Tarifa, pk=pk)
    if request.method == "POST":
        tarifa.delete()
        return redirect("lista_tarifas")
    return render(request, "tarifas/confirmar_eliminar.html", {"tarifa": tarifa})

# --- MONEDAS ---
from .models import Moneda, ModalidadTarifa, CanalVenta

def lista_monedas(request):
    monedas = Moneda.objects.all()
    return render(request, "tarifas/lista_monedas.html", {"monedas": monedas})

def crear_moneda(request):
    if request.method == "POST":
        form = MonedaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_monedas")
    else:
        form = MonedaForm()
    return render(request, "tarifas/form_moneda.html", {"form": form})

def editar_moneda(request, pk):
    moneda = get_object_or_404(Moneda, pk=pk)
    if request.method == "POST":
        form = MonedaForm(request.POST, instance=moneda)
        if form.is_valid():
            form.save()
            return redirect("lista_monedas")
    else:
        form = MonedaForm(instance=moneda)
    return render(request, "tarifas/form_moneda.html", {"form": form})

def eliminar_moneda(request, pk):
    moneda = get_object_or_404(Moneda, pk=pk)
    if request.method == "POST":
        moneda.delete()
        return redirect("lista_monedas")
    return render(request, "tarifas/confirmar_eliminar.html", {"objeto": moneda, "tipo": "Moneda"})


# --- MODALIDADES ---
def lista_modalidades(request):
    modalidades = ModalidadTarifa.objects.all()
    return render(request, "tarifas/lista_modalidades.html", {"modalidades": modalidades})

def crear_modalidad(request):
    if request.method == "POST":
        form = ModalidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_modalidades")
    else:
        form = ModalidadForm()
    return render(request, "tarifas/form_modalidad.html", {"form": form})

def editar_modalidad(request, pk):
    modalidad = get_object_or_404(ModalidadTarifa, pk=pk)
    if request.method == "POST":
        form = ModalidadForm(request.POST, instance=modalidad)
        if form.is_valid():
            form.save()
            return redirect("lista_modalidades")
    else:
        form = ModalidadForm(instance=modalidad)
    return render(request, "tarifas/form_modalidad.html", {"form": form})

def eliminar_modalidad(request, pk):
    modalidad = get_object_or_404(ModalidadTarifa, pk=pk)
    if request.method == "POST":
        modalidad.delete()
        return redirect("lista_modalidades")
    return render(request, "tarifas/confirmar_eliminar.html", {"objeto": modalidad, "tipo": "Modalidad"})


# --- CANALES ---
def lista_canales(request):
    canales = CanalVenta.objects.all()
    return render(request, "tarifas/lista_canales.html", {"canales": canales})

def crear_canal(request):
    if request.method == "POST":
        form = CanalVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_canales")
    else:
        form = CanalVentaForm()
    return render(request, "tarifas/form_canal.html", {"form": form})

def editar_canal(request, pk):
    canal = get_object_or_404(CanalVenta, pk=pk)
    if request.method == "POST":
        form = CanalVentaForm(request.POST, instance=canal)
        if form.is_valid():
            form.save()
            return redirect("lista_canales")
    else:
        form = CanalVentaForm(instance=canal)
    return render(request, "tarifas/form_canal.html", {"form": form})

def eliminar_canal(request, pk):
    canal = get_object_or_404(CanalVenta, pk=pk)
    if request.method == "POST":
        canal.delete()
        return redirect("lista_canales")
    return render(request, "tarifas/confirmar_eliminar.html", {"objeto": canal, "tipo": "Canal"})

# --- TIPO DE CAMBIO ---
def lista_tipocambio(request):
    cambios = TipoCambio.objects.select_related("moneda").order_by("-fecha")
    return render(request, "tarifas/lista_tipocambio.html", {"cambios": cambios})

def crear_tipocambio(request):
    if request.method == "POST":
        form = TipoCambioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tipocambio")
    else:
        form = TipoCambioForm()
    return render(request, "tarifas/form_tipocambio.html", {"form": form})

def editar_tipocambio(request, pk):
    cambio = get_object_or_404(TipoCambio, pk=pk)
    if request.method == "POST":
        form = TipoCambioForm(request.POST, instance=cambio)
        if form.is_valid():
            form.save()
            return redirect("lista_tipocambio")
    else:
        form = TipoCambioForm(instance=cambio)
    return render(request, "tarifas/form_tipocambio.html", {"form": form})

def eliminar_tipocambio(request, pk):
    cambio = get_object_or_404(TipoCambio, pk=pk)
    if request.method == "POST":
        cambio.delete()
        return redirect("lista_tipocambio")
    return render(request, "tarifas/confirmar_eliminar.html", {"objeto": cambio, "tipo": "Tipo de cambio"})