# Analise do projeto ALFA2-BD para o projeto ALFA3-BD

Objetivo é analisar o projeto ALFA2-BD e identificar quais serão os proximos passos para o projeto ALFA3-BD.

## Explicação da Estrutura

Banco MongoDB criado temporariamente na nuvem com configuração disponível no arquivo .env

Banco PostgreSQL criado temporariamente na nuvem com configuração disponível no arquivo .env

A criação das tabelas e collections já foram rodadas e populadas com os scripts já desenvolvidos no ALFA2-DB.

Basta fazer clone do projeto e configurar o ambiente python conforme informado abaixo.

## Configurando ambiente python

Antes de usar o ambiente, crie um ambiente virtual. Recomendo o [virtualenv](https://pypi.org/project/virtualenv/).

```shell
pip install virtualenv
```

Para criar o ambiente virtual, execute:

```shell
virtualenv venv
```

Para ativar o ambiente virtual, use:

```shell
source venv/bin/activate
```

Uma vez ativado o ambiente virtual, instale os pacotes:

```shell
pip install -r requirements.txt
```

Sempre que for instalado um novo pacote é nesse arquivo que será colocado as mudanças.

## Usando o Django

Para usar o Django há alguns comandos principais que podem ajudar no desenvolvimento.

O comando `django-admin startproject [anything_project]` criar um novo projeto Django.

O comando `python manage.py runserver` executa o servidor Django.

O comando `python manage.py migrate` ajusta as tabelas do Django ao banco de dados.

## Usando o Django Admin

Para visualzar o banco e ter controle sobre os dados o Django disponibiliza uma tela de admin para ter como auxílio. Ela está no link [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

Antes de acessar ela é importante criar um usuário admin. Para fazer isso, basta executar o comando `python manage.py createsuperuser`.

Depois disso, basta entrar no link e visualizar a tela de admin.

## Alguns dados de teste

Para fins de testes desabilitei a necessidade de senhas.

Logins para acesso como professor:
  685.723.401-90
  729.015.368-59
  284.317.506-26
  678.543.910-84
  489.732.506-47
  053.194.726-25
  653.420.197-61


Logins para acesso como gestor:
  628.951.704-01
  701.895.623-40
  361.957.284-46
  752.084.913-97
  584.371.069-66
  791.645.023-25
  085.291.734-14
