from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_habitaciones, name="lista_habitaciones"),
    path("<int:habitacion_id>/", views.detalle_habitacion, name="detalle_habitacion"),
    path("crear/", views.crear_habitacion, name="crear_habitacion"),
]
