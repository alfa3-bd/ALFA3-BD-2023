import factory
from models import UnidadeEscolar


class UnidadeEscolarFactory(factory.Factory):
    class Meta:
        model = UnidadeEscolar
    codigo_inep = factory.Faker()
    nome = factory.Faker()
    unidade_federacao = factory.Faker()
    municipio = factory.Faker()
    cep = factory.Faker()
    endereco = factory.Faker()
    categoria_administrativa = factory.Faker()
    dependencia_administrativa = factory.Faker()
