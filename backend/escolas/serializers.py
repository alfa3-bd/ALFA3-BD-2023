# Serializers define the API representation.
from rest_framework import serializers
from django.contrib.auth.models import User
from escolas.models import (
    Contrato, UnidadeEscolar,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UnidadeEscolarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadeEscolar
        fields = [
            'codigo_inep', 'nome', 'unidade_federacao', 'municipio', 'cep',
            'endereco', 'categoria_administrativa',
            'dependencia_administrativa',
        ]


class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = [
            'unidade_escolar', 'infraestrutura',
            'data_inicio', 'data_fim', 'tipo',
        ]
