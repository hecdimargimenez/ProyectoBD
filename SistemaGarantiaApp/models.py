from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula=models.CharField(max_length=30, primary_key=True)
    rif=models.CharField(max_length=30)
    nombre_clte=models.CharField(max_length=255)
    apellido_clte=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    telefono=models.CharField(max_length=30)
    estatus=models.BooleanField(default=True)

    def __str__(self):
        txt = "{0}, {1} {2}"
        return txt.format(self.cedula,self.nombre_clte,self.apellido_clte)


class Factura(models.Model):
    numero_fact=models.AutoField(primary_key=True)
    cliente_ced=models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha_emision=models.DateTimeField(auto_now_add=True)
    forma_pago=models.CharField(max_length=255)
    monto_total=models.IntegerField()
    estatus=models.BooleanField(default=True)

    def __str__(self):
        return str(self.numero_fact)


class Garantia(models.Model):
    numero_garan=models.AutoField(primary_key=True)
    factura_num=models.ForeignKey(Factura, null=False, blank=False, on_delete=models.CASCADE)
    fecha_inicio=models.DateField()
    fecha_venc=models.DateField()
    estatus=models.BooleanField(default=True)

    def __str__(self):
        return str(self.numero_garan)


class Departamento(models.Model):
    codigo_dpto=models.AutoField(primary_key=True)
    nombre_dpto=models.CharField(max_length=255)
    estatus=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_dpto


class Ticket(models.Model):
    codigo_tick=models.AutoField(primary_key=True)
    garantia_num=models.ForeignKey(Garantia, null=False, blank=False, on_delete=models.CASCADE)
    departamento_cod=models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.CASCADE)
    fecha_creac=models.DateTimeField(auto_now_add=True)
    fecha_act=models.DateTimeField(auto_now_add=True)
    tipo_falla=models.CharField(max_length=255)
    detalle_falla=models.CharField(max_length=255)
    arch_fact=models.FileField(upload_to='facturas') #Carpeta donde se guardaran las factura dentro de media
    cert_garan=models.FileField(upload_to='garantias') #Carpeta donde se guardaran las garantias dentro de media
    estatus=models.BooleanField(default=True)

    def __str__(self):
        return str(self.codigo_tick)


class Modelo(models.Model):
   codigo_mdlo=models.AutoField(primary_key=True)
   descrip_mdlo=models.CharField(max_length=255)
   estatus=models.BooleanField(default=True)

   def __str__(self):
        return self.descrip_mdlo


class Marca(models.Model):
   codigo_mar=models.AutoField(primary_key=True)
   nombre_mar=models.CharField(max_length=255)
   estatus=models.BooleanField(default=True)

   def __str__(self):
        return self.nombre_mar


class Producto(models.Model):
    codigo_prod=models.AutoField(primary_key=True)
    modelo_cod=models.ForeignKey(Modelo, null=False, blank=False, on_delete=models.CASCADE)  
    marca_cod=models.ForeignKey(Marca, null=True, blank=True, on_delete=models.CASCADE)
    nombre_prod=models.CharField(max_length=255)
    descrip_prod=models.CharField(max_length=255)
    img_prod=models.ImageField(upload_to='productos', null=True, blank=True)#Carpeta para guardar las imagenes de los productos
    existencia=models.IntegerField()
    costo=models.IntegerField()
    meses_garan=models.IntegerField()
    estatus=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_prod


class Detalle(models.Model):
    codigo_detal=models.AutoField(primary_key=True)
    factura_num=models.ForeignKey(Factura, null=False, blank=False, on_delete=models.CASCADE)
    producto_cod=models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    precio=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
        return str(self.codigo_detal)

