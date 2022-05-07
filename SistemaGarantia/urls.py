"""SistemaGarantia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from SistemaGarantiaApp import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('productos', views.productos, name="Productos"),
    path('contacto', views.contacto, name="Contacto"),
    path('reclamos', views.reclamos, name="Reclamos"),
    path('incluirTicket/', views.incluirTickets, name="Incluir Tickets"),
    path('eliminarTicket/<codigo>', views.eliminarTickets, name="Eliminar Tickets"),
    path('editarTicket/<codigo>', views.editarTickets, name="Editar Tickets"),
    path('busqueda/', views.buscarTicket, name="Incluir Tickets"),
    #path('edicionTickets/', views.edicionTickets, name="Edicion Tickets"),



]

#Ruta para los archivos media 

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
