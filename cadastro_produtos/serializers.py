from rest_framework import serializers
from cadastro_produtos import models


class CadastramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadastramento
        fields = '__all__'