from django.contrib.auth.models import User
from rest_framework import viewsets

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

# class Relatorio(viewsets)