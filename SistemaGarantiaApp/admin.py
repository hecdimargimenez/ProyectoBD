from msilib.schema import Class
from django.contrib import admin
from .models import * #Importamos todos los modelos 

# Register your models here.

class SistemaGarantiaAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creac','fecha_act','fecha_emision')

admin.site.register(Cliente)
admin.site.register(Factura, SistemaGarantiaAdmin)
admin.site.register(Garantia)
admin.site.register(Departamento)
admin.site.register(Ticket,SistemaGarantiaAdmin)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Detalle)

