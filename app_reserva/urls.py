from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_reservas, name="lista_reservas"),
    path("crear/", views.crear_reserva, name="crear_reserva"),
    path("editar/<int:pk>/", views.editar_reserva, name="editar_reserva"),
]
