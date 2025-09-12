from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_habitaciones, name="lista_habitaciones"),
    path("<int:habitacion_id>/", views.detalle_habitacion, name="detalle_habitacion"),
    path("crear/", views.crear_habitacion, name="crear_habitacion"),
    path("crear_tipo/", views.crear_tipo_habitacion, name="crear_tipo_habitacion"),
    path("tipos/", views.lista_tipo_habitacion, name="lista_tipo_habitacion"),
    path("tipos/<int:pk>/editar/", views.editar_tipo_habitacion, name="editar_tipo_habitacion"),
    path("tipos/<int:pk>/eliminar/", views.eliminar_tipo_habitacion, name="eliminar_tipo_habitacion"),
    path("<int:habitacion_id>/editar/", views.editar_habitacion, name="editar_habitacion"),
    path("<int:habitacion_id>/eliminar/", views.eliminar_habitacion, name="eliminar_habitacion"),
]
