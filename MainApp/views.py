from django.shortcuts import render,redirect
from producto.models import Producto

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html')

def buscar(request):

    nom = request.GET['busqueda'].capitalize()
    if request.GET['busqueda']:
        productos = Producto.objects.filter(nombre__icontains=nom)
                 
        return render(request,"mainapp/resultadobusqueda.html", {'productos':productos})         
            
    else:
        
        return redirect('/')
        