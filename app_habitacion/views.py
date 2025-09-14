from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Habitacion, TipoHabitacion
from django.contrib import messages
from .models import Habitacion, TipoHabitacion
from .forms import HabitacionForm, TipoHabitacionForm

def lista_habitaciones(request):
    estado = request.GET.get("estado")
    queryset = Habitacion.objects.exclude(estado="BAJA")  # no mostramos eliminadas

    if estado:
        queryset = queryset.filter(estado=estado)

    habitaciones = queryset.select_related("tipo_habitacion")
    
    # Mapeo de estados a clases CSS de color
    estado_colores = {
        'DISPONIBLE': 'success',
        'OCUPADA': 'info',
        'EN MANTENIMIENTO': 'danger',
        'RESERVADA': 'info',
        'LIMPIEZA': 'secondary',
        'SIN USO': 'muted',
    }
    
    # Asignar la clase de color a cada objeto de habitación
    for habitacion in habitaciones:
        # Se usa .get() para evitar un error si el estado no está en el diccionario.
        # Si no se encuentra, la clase por defecto será 'muted'.
        habitacion.color = estado_colores.get(habitacion.estado, 'muted')
        
        
    # Esta línea es la clave para diferenciar peticiones HTMX.
    if request.headers.get("HX-Request"):
        return render(request, "habitacion/_lista_habitaciones.html", {
            "habitaciones": habitaciones,
            "estado": estado,
        })
    
    # Si no es una petición HTMX, renderiza la página completa.
    return render(request, "habitacion/lista_habitaciones.html", {
        "habitaciones": habitaciones,
        "estado": estado,
    })




def detalle_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    
    if request.headers.get("HX-Request")==True:
        return render(request, "habitacion/_detalle.html", {"habitacion": habitacion})
    return render(request, "habitacion/detalle.html", {"habitacion": habitacion})

# Vista para CREAR una habitación (usando HTMX)
def crear_habitacion(request):
    # Lógica para manejar la petición POST (tanto HTMX como normal)
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Habitación creada con éxito!")
            # Si es HTMX, devolvemos un formulario vacío para que el usuario pueda crear otro
            if request.headers.get("HX-Request"):
                return HttpResponse(headers={"HX-Redirect": reverse("lista_habitaciones")})
            else:
                # Si no es HTMX, redirigimos a la lista de habitaciones
                return HttpResponseRedirect(reverse("lista_habitaciones"))
        else:
            # Si el formulario no es válido, renderizamos el formulario con errores
            # para HTMX o para un POST normal.
            return render(request, "habitacion/_formulario.html", {
                "form": form,
                "es_edicion": False,
            }, status=422)

    # Lógica para la petición GET (tanto HTMX como normal)
    form = HabitacionForm()
    if request.headers.get("HX-Request"):
        return render(request, "habitacion/_formulario.html", {
            "form": form,
            "es_edicion": False,
        })
    else:
        # Petición GET normal
        return render(request, "habitacion/crear_editar_habitacion.html", {
            "form": form,
            "es_edicion": False,
        })


def editar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    
    # Maneja las peticiones POST de HTMX y no-HTMX
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Habitación actualizada con éxito!")
            
            # Si la petición POST es de HTMX, devuelve un encabezado de redirección.
            if request.headers.get("HX-Request"):
                response = HttpResponseRedirect(reverse("lista_habitaciones"))
                response['HX-Redirect'] = reverse("lista_habitaciones")
                return response
            else:
                # Si es un POST normal, redirige directamente.
                return HttpResponseRedirect(reverse("lista_habitaciones"))
        else:
            # Si el formulario es inválido, devuelve el mismo formulario con errores.
            if request.headers.get("HX-Request"):
                return render(request, "habitacion/_formulario.html", {
                    "form": form,
                    "es_edicion": True,
                    "habitacion": habitacion,  # <-- Se pasa el objeto habitacion
                }, status=422)
            else:
                return render(request, "habitacion/crear_editar_habitacion.html", {
                    "form": form,
                    "es_edicion": True,
                    "habitacion": habitacion,  # <-- Se pasa el objeto habitacion
                })
    else:
        # Petición GET
        form = HabitacionForm(instance=habitacion)

    # Si la petición GET es de HTMX, devuelve el fragmento del formulario.
    if request.headers.get("HX-Request"):
        return render(request, "habitacion/_formulario.html", {
            "form": form,
            "es_edicion": True,
            "habitacion": habitacion, # <-- Se pasa el objeto habitacion
        })

    # Si es un GET normal, devuelve la página completa.
    return render(request, "habitacion/crear_editar_habitacion.html", {
        "form": form,
        "es_edicion": True,
        "habitacion": habitacion, # <-- Se pasa el objeto habitacion
    })

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