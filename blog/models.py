from django.db import models
from django.utils import timezone

class Tecnico( models.Model ):
    id_tecnico = models.AutoField( 
        primary_key = True )
    nombre_tecnico = models.CharField( 
        max_length = 255, blank = False , null = False )
    correo = models.CharField(
         max_length = 255, blank = False , null = False )
    contraseña = models.CharField( 
        max_length = 16, blank = False, null = False )
    def __str__(self):
        return self.nombre_tecnico
class Cliente(models.Model):
    id_cliente = models.AutoField( 
        primary_key = True )
    nombre_cliente = models.CharField( 
        max_length = 255, blank = False , null = False )
    direccion_cliente = models.CharField( 
        max_length = 255, blank = False , null = False )
    ciudad_cliente = models.CharField( 
        max_length = 255, blank = False , null = False )
    comuna_cliente = models.CharField( 
        max_length = 255, blank = False , null = False )
    telefono_cliente = models.IntegerField()
    correo_cliente = models.CharField( 
        max_length = 255, blank = False , null = False )
    def __str__(self):
        return self.nombre_cliente

class Tarea(models.Model):
    tarea_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, blank = False, null = False, on_delete = models.CASCADE )
    fecha = models.DateField(
            default=timezone.now)
    inicio_atencion = models.TimeField(
            blank=True, null=False)
    termino_atencion = models.TimeField(
            blank=True, null=False)
    id_ascensor = models.CharField(max_length=63)
    modelo_ascensor = models.CharField(max_length=255)
    fallas_detectadas = models.TextField()
    reparaciones_efectuadas = models.TextField()
    piezas_cambiadas = models.TextField()
    tecnico = models.ForeignKey(Tecnico, blank = False, null = False, on_delete = models.CASCADE )
    def publish(self):
        self.termino_atencion = timezone.now()
        self.save()