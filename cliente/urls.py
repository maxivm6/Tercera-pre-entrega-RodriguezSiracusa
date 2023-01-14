from django.urls import path
from . import views
from MainApp.views import buscar

#Path al view cliente y a la barra buscador que es comun en todas las apps


urlpatterns = [
    path('', views.cliente_formulario, name='Formulario'),
    path('',buscar,name="buscar"),
]