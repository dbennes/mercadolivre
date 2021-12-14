from django.db.models import fields
from rest_framework import serializers
from ordemfila.models import ordem_fila

class OrdemFilaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ordem_fila
        fields = ['fila', 'nome_usuario', 'posicao', 'vaga', 'posicao2', 'posicao3']