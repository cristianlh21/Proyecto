from django.urls import path
from app_reserva import views

urlpatterns = [
    # Lista de reservas
    path('', views.lista_reservas, name='lista_reservas'),

    # Crear reserva
    path('crear/', views.crear_reserva, name='crear_reserva'),

    # Editar reserva básica
    path('editar/<int:pk>/', views.editar_reserva, name='editar_reserva'),

    # Editar reserva completo (habitaciones + huéspedes)
    path('editar/<int:pk>/completo/', views.editar_reserva_completo, name='editar_reserva_completo'),

    # Agregar habitación a la reserva
    path('editar/<int:reserva_pk>/habitacion/', views.agregar_habitacion_reserva, name='agregar_habitacion_reserva'),

    # Agregar huésped a una habitación de la reserva
    path('habitacion/<int:reserva_habitacion_pk>/huesped/', views.agregar_huesped_habitacion, name='agregar_huesped_habitacion'),
]
