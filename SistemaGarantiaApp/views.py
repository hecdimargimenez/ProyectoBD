import email
from logging import exception
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import HttpResponse
from matplotlib.pyplot import get
from .models import *
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError


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
    ticketsListados=Ticket.objects.all()
    return render(request, "SistemaGarantia/reclamos.html", {"tickets": ticketsListados})

#Función que incluye un ticket
def incluirTickets(request):
    ticket=Ticket()
    #nombre = request.POST['txtNombre']
    #email = request.POST['txtEmail']
    #tlf = request.POST['txtTlf']
    #nroF = request.POST['txtNroF']
    ticket.garantia_num=Garantia.objects.get(numero_garan = request.POST['txtNroG'])
    ticket.tipo_falla=request.POST['tipoFalla']
    ticket.departamento_cod=Departamento.objects.get(nombre_dpto=request.POST['departamento'])
    ticket.detalle_falla=request.POST['txtDetalle']
    ticket.arch_fact=request.POST['fileF']
    ticket.cert_garan=request.POST['fileG']
    ticket.save()
    messages.success(request, 'Ticket Enviado!')
    return redirect('/reclamos')

#Función que elimina un ticket
def eliminarTickets(request, codigo):
    ticket=Ticket.objects.get(codigo_tick=codigo)
    ticket.delete()
    messages.success(request, 'Ticket Eliminado!')

    return redirect('/reclamos')
    
#Función que edita un ticket
def editarTickets(request, codigo):
    ticket=Ticket.objects.get(codigo_tick=codigo)
    #ticket=get_object_or_404(Ticket, codigo_tick=codigo)  
    if request.method=='GET' :
        datos={'tipo_falla':ticket.tipo_falla, 'departamento_cod': ticket.departamento_cod,
               'detalle_falla': ticket.detalle_falla, 'arch_fact':ticket.arch_fact,
               'cert_garan': ticket.cert_garan}    
        return render(request, "SistemaGarantia/edicionTicket.html", {"ticket": ticket})
    if request.method=='POST':
        ticket.garantia_num=Garantia.objects.get(numero_garan = request.POST['txtNroG'])
        ticket.tipo_falla=request.POST['tipoFalla']
        ticket.departamento_cod=Departamento.objects.get(nombre_dpto=request.POST['departamento'])
        ticket.detalle_falla=request.POST['txtDetalle']
        ticket.arch_fact=request.POST['fileF']
        ticket.cert_garan=request.POST['fileG']
        ticket.save()
        return render(request, "SistemaGarantia/reclamos.html")
    
    
    #return render(request, "SistemaGarantia/edicionTicket.html", {"ticket": ticket})

#Función que edita un ticket

"""" def edicionTickets(request):
    ticket=Ticket()
    nombre = request.POST['txtNombre']
    email = request.POST['txtEmail']
    tlf = request.POST['txtTlf']
    nroF = request.POST['txtNroF']
    ticket.garantia_num=Garantia.objects.get(numero_garan = request.POST['txtNroG'])
    ticket.tipo_falla=request.POST['tipoFalla']
    ticket.departamento_cod=Departamento.objects.get(nombre_dpto=request.POST['departamento'])
    ticket.detalle_falla=request.POST['txtDetalle']
    ticket.arch_fact=request.POST['fileF']
    ticket.cert_garan=request.POST['fileG']
    
    ticket=Ticket.objects.get(codigo_tick=codigo)
    ticket.save()
    return redirect('/reclamos') """
    

def buscarTicket(request):

    if request.GET["txtBuscar"]:
         
        tick=request.GET["txtBuscar"]
        tickets=Ticket.objects.filter(codigo_tick__icontains=tick)
       
        return render(request, "SistemaGarantia/busqueda.html", {"tickets":tickets, "query":tick})

    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)
   