from django.urls import path
from . import views

urlpatterns = [
    path('', views.empleado_formulario, name='Empleado'),
]