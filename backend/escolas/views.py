from django.contrib.auth.models import User
from rest_framework import viewsets

from escolas.models import Contrato, UnidadeEscolar
from escolas.serializers import (
    ContratoSerializer, UnidadeEscolarSerializer, UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UnidadeEscolar(viewsets.ModelViewSet):
    queryset = UnidadeEscolar.objects.all()
    serializer_class = UnidadeEscolarSerializer


class Contrato(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

# class Relatorio(viewsets)