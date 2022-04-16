from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home")

def nosotros(request):
    return HttpResponse("Nosotros")

def productos(request):
    return HttpResponse("Productos")

def contacto(request):
    return HttpResponse("Contacto")

def reclamos(request):
    return HttpResponse("Reclamos")