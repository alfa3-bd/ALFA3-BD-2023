# Serializers define the API representation.
from rest_framework import serializers
from django.contrib.auth.models import User
from escolas import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UnidadeEscolarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UnidadeEscolar
        fields = [
            'codigo_inep', 'nome', 'unidade_federacao', 'municipio', 'cep',
            'endereco', 'categoria_administrativa',
            'dependencia_administrativa',
        ]


class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contrato
        fields = [
            'unidade_escolar', 'infraestrutura',
            'data_inicio', 'data_fim', 'tipo',
        ]

class InfraestruturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Infraestrutura
        fields = [
            'nome_cluster', 'nivel_governamental', 'nome_provedor',
        ]

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Node
        fields = [
            'node_ip', 'node_port',
        ]
