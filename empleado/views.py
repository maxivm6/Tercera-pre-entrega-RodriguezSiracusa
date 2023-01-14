from django.shortcuts import render,redirect
from .models import Empleado
from .forms import FormEmpleado

# Create your views here.
def empleado_formulario(request):
    formulario = FormEmpleado(request.POST or None)
    if request.method == 'POST':
        
        
        try:
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                empleado = Empleado (nombre=informacion['nombre'],
                                     apellido=informacion['apellido'],
                                     salario=informacion['salario'],
                                     area=informacion['area'],)
                empleado.save()
                
                return redirect("/empleado/?ok")
            else:
                return redirect("/empleado/?fail")
        except:
            return redirect("/empleado/?fail")
        
    return render(request,"empleado/empleado.html", {"miFormulario":formulario})