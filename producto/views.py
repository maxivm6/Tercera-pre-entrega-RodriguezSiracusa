from django.shortcuts import render, redirect
from .models import Producto
from .forms import FormProducto

# Create your views here.
def producto_formulario(request):
    formulario = FormProducto(request.POST or None)
    if request.method == 'POST':
        
        
        try:
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                producto = Producto (nombre=informacion['nombre'],
                                     descripcion=informacion['descripcion'],
                                     precio=informacion['precio'],
                                     stock=informacion['stock'],
                                    )
                producto.save()
                
                return redirect("/producto/?ok")
            else:
                return redirect("/producto/?fail")
        except:
            return redirect("/producto/?fail")
        
    return render(request,"producto/producto.html", {"miFormulario":formulario})


