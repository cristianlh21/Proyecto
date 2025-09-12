from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_huespedes, name="lista_huespedes"),
    path("crear/", views.crear_huesped, name="crear_huesped"),
    path("editar/<int:pk>/", views.editar_huesped, name="editar_huesped"),
]
