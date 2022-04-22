from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Producto

# Create your views here.

def home(request):
    return render(request, "SistemaGarantia/home.html")

def nosotros(request):
    return render(request, "SistemaGarantia/nosotros.html")

def productos(request):
    productos=Producto.objects.all()
    return render(request, "SistemaGarantia/productos.html", {"productos":productos})

def contacto(request):
    return render(request, "SistemaGarantia/contacto.html")

def reclamos(request):
    return render(request, "SistemaGarantia/reclamos.html")
