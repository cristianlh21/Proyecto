from django.urls import path
from . import views

urlpatterns = [
    # Tarifas
    path("", views.lista_tarifas, name="lista_tarifas"),
    path("crear/", views.crear_tarifa, name="crear_tarifa"),
    path("editar/<int:pk>/", views.editar_tarifa, name="editar_tarifa"),
    path("eliminar/<int:pk>/", views.eliminar_tarifa, name="eliminar_tarifa"),

    # Monedas
    path("monedas/", views.lista_monedas, name="lista_monedas"),
    path("monedas/crear/", views.crear_moneda, name="crear_moneda"),
    path("monedas/editar/<int:pk>/", views.editar_moneda, name="editar_moneda"),
    path("monedas/eliminar/<int:pk>/", views.eliminar_moneda, name="eliminar_moneda"),

    # Modalidades
    path("modalidades/", views.lista_modalidades, name="lista_modalidades"),
    path("modalidades/crear/", views.crear_modalidad, name="crear_modalidad"),
    path("modalidades/editar/<int:pk>/", views.editar_modalidad, name="editar_modalidad"),
    path("modalidades/eliminar/<int:pk>/", views.eliminar_modalidad, name="eliminar_modalidad"),

    # Canales
    path("canales/", views.lista_canales, name="lista_canales"),
    path("canales/crear/", views.crear_canal, name="crear_canal"),
    path("canales/editar/<int:pk>/", views.editar_canal, name="editar_canal"),
    path("canales/eliminar/<int:pk>/", views.eliminar_canal, name="eliminar_canal"),
    
    # TipoCambio
    path("tipocambio/", views.lista_tipocambio, name="lista_tipocambio"),
    path("tipocambio/crear/", views.crear_tipocambio, name="crear_tipocambio"),
    path("tipocambio/editar/<int:pk>/", views.editar_tipocambio, name="editar_tipocambio"),
    path("tipocambio/eliminar/<int:pk>/", views.eliminar_tipocambio, name="eliminar_tipocambio"),

]
