from django.contrib import admin
from .models import * #Importamos todos los modelos 

#Clases para mostrar los campos en modo lectura
class TicketAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creac','fecha_act')

class FacturaAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_emision',)

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('codigo_prod',)
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Garantia)
admin.site.register(Departamento)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle)

