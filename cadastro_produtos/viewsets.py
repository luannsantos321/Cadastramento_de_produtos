from rest_framework import viewsets
from cadastro_produtos import models
from cadastro_produtos import serializers


class CadastramentoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CadastramentoSerializer
    queryset = models.Cadastramento.objects.all()
