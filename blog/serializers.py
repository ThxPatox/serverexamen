from .models import *
from rest_framework import serializers

class TecnicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('id_tecnico','nombre_tecnico','correo','contraseña')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id_cliente','nombre_cliente','direccion_cliente','ciudad_cliente','comuna_cliente','telefono_cliente','correo_cliente')
        
class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarea
        fields = ('tarea_id','cliente','fecha','inicio_atencion',
        'termino_atencion','id_ascensor','modelo_ascensor','fallas_detectadas',
        'reparaciones_efectuadas','piezas_cambiadas','tecnico')