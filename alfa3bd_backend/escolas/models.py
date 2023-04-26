from djongo import models


class UnidadeEscolar(models.Model):
    codigo_inep = models.IntegerField(unique=True)
    nome = models.CharField(unique=True, max_length=50)
    unidade_federacao = models.CharField(max_length=2)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=50)
    categoria_administrativa = models.IntegerField()
    dependencia_administrativa = models.IntegerField()


class Infraestrutura(models.Model):
    nome_cluster = models.CharField(null=False, max_length=30)
    nivel_governamental = models.IntegerField(null=False)
    nome_provedor = models.CharField(null=False, max_length=255)


class Node(models.Model):
    infraestrutura = models.ForeignKey(
        Infraestrutura, on_delete=models.DO_NOTHING, related_name='nodes')
    node_ip = models.CharField(null=False, max_length=15)
    node_port = models.IntegerField(null=False)


class Contrato(models.Model):
    unidade_escolar = models.ForeignKey(
        UnidadeEscolar, on_delete=models.DO_NOTHING, related_name='contratos')
    infraestrutura = models.ForeignKey(
        Infraestrutura, on_delete=models.DO_NOTHING, related_name='contrato')

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    tipo = models.IntegerField(unique=True)
