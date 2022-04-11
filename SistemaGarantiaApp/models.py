from django.db import models

# Create your models here.

class Ticket(models.Model):
    cod_ticket=models.CharField(max_length=20, primary_key=True)
    cod_garantia=models.CharField(max_length=20)
    cod_departamento=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    tipo_falla=models.CharField(max_length=50)
    detalle_falla=models.CharField(max_length=300)
    arch_factura=models.FileField()
    cert_garantia=models.FileField()
    estatus=models.BooleanField(default=True)


class Cliente(models.Model):
    cedula=models.CharField(max_length=15, primary_key=True)
    rif=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    telefono=models.CharField(max_length=20)
    estatus=models.BooleanField(default=True)