from django.shortcuts import render,redirect
from .forms import FormCliente
from .models import Cliente

# Create your views here.

def cliente_formulario(request):
    formulario = FormCliente(request.POST)
    if request.method == 'POST':
        
        
        try:
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                cliente = Cliente (nombre=informacion['nombre'],
                                   apellido=informacion['apellido'],
                                   email=informacion['email'],
                                   telefono=informacion['telefono'],
                                   direccion=informacion['direccion'],)
                cliente.save()
                
                return redirect("/cliente/?ok")
            else:
                return redirect("/cliente/?fail")
        except:
            return redirect("/cliente/?fail")
        
    return render(request,"cliente/cliente.html", {"miFormulario":formulario})