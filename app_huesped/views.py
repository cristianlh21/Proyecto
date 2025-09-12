from django.shortcuts import render, redirect, get_object_or_404
from .models import Huesped
from .forms import HuespedForm

def lista_huespedes(request):
    huespedes = Huesped.objects.all()
    return render(request, "huesped/lista_huespedes.html", {"huespedes": huespedes})

def crear_huesped(request):
    if request.method == "POST":
        form = HuespedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_huespedes")
    else:
        form = HuespedForm()
    return render(request, "huesped/form_huesped.html", {"form": form})

def editar_huesped(request, pk):
    huesped = get_object_or_404(Huesped, pk=pk)
    if request.method == "POST":
        form = HuespedForm(request.POST, instance=huesped)
        if form.is_valid():
            form.save()
            return redirect("lista_huespedes")
    else:
        form = HuespedForm(instance=huesped)
    return render(request, "huesped/form_huesped.html", {"form": form})
