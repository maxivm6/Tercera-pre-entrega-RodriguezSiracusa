from django.urls import path
from . import views
from MainApp.views import buscar

urlpatterns = [
    path('', views.empleado_formulario, name='Empleado'), 
    path('buscar/',buscar,name="buscar"),
]