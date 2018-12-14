from .models import *
from rest_framework import viewsets
from .serializers import *

class ClienteViewSet( viewsets.ModelViewSet ):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TecnicoViewSet( viewsets.ModelViewSet ):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class TareaViewSet( viewsets.ModelViewSet ):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer