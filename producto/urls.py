from django.urls import path
from . import views
from MainApp.views import buscar

urlpatterns = [
    path('', views.producto_formulario, name='Producto'),
    path('buscar/',buscar,name="buscar"),
]