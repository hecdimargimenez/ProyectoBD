from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request, "SistemaGarantia/home.html")

def nosotros(request):
    return render(request, "SistemaGarantia/nosotros.html")

def productos(request):
    return render(request, "SistemaGarantia/productos.html")

def contacto(request):
    return render(request, "SistemaGarantia/contacto.html")

def reclamos(request):
    return render(request, "SistemaGarantia/reclamos.html")
