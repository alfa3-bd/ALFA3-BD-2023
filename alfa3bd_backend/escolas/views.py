from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from escolas import models
from escolas import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UnidadeEscolar(viewsets.ModelViewSet):
    queryset = models.UnidadeEscolar.objects.all()
    serializer_class = serializers.UnidadeEscolarSerializer


class Contrato(viewsets.ModelViewSet):
    queryset = models.Contrato.objects.all()
    serializer_class = serializers.ContratoSerializer


class Node(viewsets.ModelViewSet):
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer


class Infraestrutura(viewsets.ModelViewSet):
    queryset = models.Infraestrutura.objects.all()
    serializer_class = serializers.NodeSerializer


class Relatorio(viewsets.ViewSet):
    serializer_class = serializers.ObjectSerializer

    def list(self, request):

        escolas_com_infra = models.UnidadeEscolar.objects.filter(
            contratos__data_fim__gte=timezone.now().date()
        ).count()

        total_escolas = models.UnidadeEscolar.objects.all().count()
        escolas_sem_infra = total_escolas - escolas_com_infra

        escola_infraestrutura = {
            'nome': 'escolas_atendidas',
            'escolas_sem_infra': escolas_sem_infra,
            'escolas_com_infra': escolas_com_infra
        }

        list_relatorio = [escola_infraestrutura]

        return Response(list_relatorio)
