"""TerceraEntrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


#Cada App tiene su archivo urls.py y desde este archivo se incluye todos para una mejor organizacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MainApp.urls')),
    path('cliente/', include('cliente.urls')),
    path('empleado/', include('empleado.urls')),
    path('producto/', include('producto.urls')),
]
