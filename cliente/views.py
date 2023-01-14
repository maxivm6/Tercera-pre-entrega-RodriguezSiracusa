from django.shortcuts import render,redirect
from .forms import FormCliente
from .models import Cliente



#Formulario que, si no recibe un request POST carga el template con el form vacio. 
#Si recibe resquest POST chequea si el form es valido y segun el resultado guarda en BD o redirige a un template con el mensaje correspondiente
#Similar en todas las clases

def cliente_formulario(request):      
    formulario = FormCliente(request.POST or None)
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