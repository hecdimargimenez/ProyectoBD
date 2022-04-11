from ssl import create_default_context
from django.db import models

# Create your models here.

class Ticket(models.Model):
    cod_ticket=models.CharField(max_length=20, primary_key=True)
    cod_garantia=models.CharField(max_length=20)
    cod_departamento=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    tipo_falla=models.CharField(max_length=20)
    detalle_falla=models.CharField(max_length=20)
    arch_factura=models.FileField()
    cert_garantia=models.FileField()
    estatus=models.BooleanField(default=True)
