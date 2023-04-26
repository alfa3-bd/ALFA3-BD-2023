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


class RelatorioSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=256)
    escolas_sem_infra = serializers.IntegerField()
    escolas_com_infra = serializers.IntegerField()


class ObjectSerializer(serializers.BaseSerializer):
    """
    A read-only serializer that coerces arbitrary complex objects
    into primitive representations.
    """

    def to_representation(self, obj):
        for attribute_name in dir(obj):
            attribute = getattr(obj, attribute_name)
            output = {}
            if attribute_name.startswith('_'):
                # Ignore private attributes.
                pass
            elif hasattr(attribute, '__call__'):
                # Ignore methods and other callables.
                pass
            elif isinstance(attribute, (str, int, bool, float, type(None))):
                # Primitive types can be passed through unmodified.
                output[attribute_name] = attribute
            elif isinstance(attribute, list):
                # Recursively deal with items in lists.
                output[attribute_name] = [
                    self.to_representation(item) for item in attribute
                ]
            elif isinstance(attribute, dict):
                # Recursively deal with items in dictionaries.
                output[attribute_name] = {
                    str(key): self.to_representation(value)
                    for key, value in attribute.items()
                }
            else:
                # Force anything else to its string representation.
                output[attribute_name] = str(attribute)

    def to_internal_value(self, data):
        return self.to_representation(data)

    def is_valid(self):
        self.data = self.initial_data
        return True


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
