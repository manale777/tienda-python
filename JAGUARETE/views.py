from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Producto, Categoria
from .forms import *
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "tienda/index.html",{
        "productos": Producto.objects.all(),
        "categorias": Categoria.objects.all()
    })

def acerca_de(request):
    return render(request, "tienda/acerca-de.html",{
        "categorias": Categoria.objects.all()
    })

def contacto(request):
    return render(request, "tienda/contacto.html",{
        "categorias": Categoria.objects.all()
    })

def nuevo_producto(request):
    if request.method == 'POST':
        form = FormProducto(request.POST, request.FILES, instance=Producto(imagen = request.FILES['imagen']))
        if form.is_valid():
            form.save()
            return redirect("JAGUARETE:index")
    else:
        return render(request, "tienda/nuevo_producto.html",{
        "categorias": Categoria.objects.all()
        })

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if request.method == "POST":
        form = FormProducto(data = request.POST, files = request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("JAGUARETE:index")
    else:
        form = FormProducto(instance=producto)
        return render(request, 'tienda/editar_producto.html',{
            "producto": producto,
            "categorias": Categoria.objects.all(),
            "form": form
        }) 

def producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    return render(request, 'tienda/producto.html',{
        "producto": producto
    })