from django.urls import path
from .views import (
    ContactoListView, ContactoCreateView, 
    ContactoUpdateView, ContactoDeleteView, 
    RegistroUsuarioView
)

urlpatterns = [
    # Rutas para la gestión de contactos
    path('', ContactoListView.as_view(), name='contacto_list'),
    path('nuevo/', ContactoCreateView.as_view(), name='contacto_create'),
    path('editar/<int:pk>/', ContactoUpdateView.as_view(), name='contacto_update'),
    path('eliminar/<int:pk>/', ContactoDeleteView.as_view(), name='contacto_delete'),
    path('usuarios/nuevo/', RegistroUsuarioView.as_view(), name='usuario_create'),
]