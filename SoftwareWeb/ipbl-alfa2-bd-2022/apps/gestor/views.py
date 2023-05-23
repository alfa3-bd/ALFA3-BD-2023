#from xxlimited import Null
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from dataset.ScriptsMongoDB import ScriptsMongoDB
from utils.DictHelper import DictHelper
from utils.CryptoHelper import CryptoHelper
from bson.objectid import ObjectId
import datetime
import json
from random import randint
import core.models

#Login
def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('gestor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def logoff(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('identificador_gestor')

    return response

def verify_login(request):

    crypto = CryptoHelper()

    context = {
        'segment': 'login',
        'err':''
    }

    if len(request.POST['identificador_gestor']):

        data = request.POST
        gestor = core.models.GestorEscola.objects.get(ges_identificador = data['identificador_gestor'])

        print(gestor.ges_identificador)
        print(crypto.decrypt_message(gestor.ges_senha))

        if len(gestor.ges_identificador) and (crypto.decrypt_message(gestor.ges_senha) == data['senha_gestor']):

            context = {
                'segment': 'home',
                'err':''
            }

            response = redirect('/gestor/home', context)
            response.set_cookie('identificador_gestor', gestor.ges_identificador)
            return response

    return redirect('/gestor/login', context)

def home(request):

    context = {
        'segment': 'home'
    }

    identificador = request.COOKIES.get('identificador_gestor')

    if identificador is not None:

        html_template = loader.get_template('gestor/screens/home.html')

        response = HttpResponse(html_template.render(context, request))
        response.set_cookie('identificador_gestor', identificador)

        return HttpResponse(html_template.render(context, request))

    else:
        context = {
            'segment': 'login',
            'err':''
        }

        return redirect('/gestor/login', context)

def informacoes(request):

    identificador = request.COOKIES.get('identificador_gestor')

    gestor = core.models.GestorEscola.objects.get(ges_identificador = identificador)

    context = {
        'segment': 'informacoes',
        'gestor': gestor,
    }

    html_template = loader.get_template('gestor/screens/informacoes.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

# Professores
def professores(request):

    identificador = request.COOKIES.get('identificador_gestor')

    professores = core.models.Professor.objects.raw("SELECT p.pro_id, p.pro_primeiro_nome, "+
    "p.pro_segundo_nome, string_agg(CONCAT('Ano: ',tur_ano,' Serie: ', tur_ano_escolar), ', ') AS turmas "+
    "FROM professor AS p LEFT JOIN turma AS t ON t.pro_id = p.pro_id GROUP BY p.pro_id ORDER BY p.pro_id");

    context = {
        'segment': 'professores',
        'professores': professores,
    }

    html_template = loader.get_template('gestor/screens/professores.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def add_professores(request):

    context = {
        'segment': 'professores',
        'err':''
    }
     
    html_template = loader.get_template('gestor/screens/add_professores.html')
    response = HttpResponse(html_template.render(context, request))
    return response

def edit_professores(request,id):

    crypto = CryptoHelper()
    
    professor = core.models.Professor.objects.get(pro_id = id)
    professor.pro_senha = crypto.decrypt_message(professor.pro_senha)

    context = {
        'segment': 'professores',
        'professor': professor,
    }

    html_template = loader.get_template('gestor/screens/edit_professores.html')
    response = HttpResponse(html_template.render(context, request))

    return response

def save_professores(request):

    crypto = CryptoHelper()

    context = {
        'segment': 'professores',
        'err':''
    }

    if 'id_prof' in request.POST:
        professor = core.models.Professor.objects.get(pro_id = request.POST["id_prof"])
        professor.pro_primeiro_nome = request.POST["fst_name_prof"]
        professor.pro_segundo_nome = request.POST["scn_name_prof"]
        professor.pro_identificador = request.POST["cpf"]
        professor.pro_senha = crypto.encrypt_message(request.POST["password"])
        professor.save()
    
    else:
        core.models.Professor.objects.create(pro_primeiro_nome=request.POST["fst_name_prof"],
                                        pro_segundo_nome = request.POST["scn_name_prof"],
                                        pro_identificador = request.POST["cpf"],
                                        pro_senha = crypto.encrypt_message(request.POST["password"]))

    response = redirect('/gestor/professores', context)

    return response

def delete_professores(request,id):
    context = {
        'segment': 'professores',
        'err':''
    }

    professor = core.models.Professor.objects.get(pro_id = id)
    professor.delete()

    response = redirect('/gestor/professores', context)

    return response

# Alunos
def alunos(request):

    alunos = core.models.Aluno.objects.all().select_related().order_by('alu_primeiro_nome')

    context = {
        'segment': 'alunos',
        'alunos': alunos,
    }

    html_template = loader.get_template('gestor/screens/alunos.html')
    response = HttpResponse(html_template.render(context, request))

    return response

def add_alunos(request):

    turmas = core.models.Turma.objects.all()
    tipo_alunos = core.models.TipoAluno.objects.all()

    context = {
        'segment': 'alunos',
        'turmas':turmas,
        'tipo_alunos':tipo_alunos,
    }

    html_template = loader.get_template('gestor/screens/add_alunos.html')
    response = HttpResponse(html_template.render(context, request))
    return response

def edit_alunos(request,id):

    aluno = core.models.Aluno.objects.get(alu_id = id)
    turmas = core.models.Turma.objects.all()
    tipo_alunos = core.models.TipoAluno.objects.all()
    
    context = {
        'segment': 'alunos',
        'aluno': aluno,
        'turmas':turmas,
        'tipo_alunos':tipo_alunos,
    }

    html_template = loader.get_template('gestor/screens/edit_alunos.html')
    response = HttpResponse(html_template.render(context, request))

    return response

def save_alunos(request):

    context = {
        'segment': 'alunos',
        'err':''
    }

    if 'id_aluno' in request.POST:
        aluno = core.models.Aluno.objects.get(alu_id = request.POST["id_aluno"])
        aluno.alu_primeiro_nome=request.POST["fst_name_aluno"]
        aluno.alu_segundo_nome = request.POST["scn_name_aluno"]
        aluno.alu_data_nascimento = datetime.datetime.strptime(str(request.POST["date_nasc_aluno"]),'%d/%m/%Y').strftime('%Y-%m-%d')
        aluno.turma = core.models.Turma(tur_id = request.POST["turma"])
        aluno.tipo = core.models.TipoAluno(tip_alu_id = request.POST["tipo"])
        aluno.save()
    
    else:
        core.models.Aluno.objects.create(alu_primeiro_nome=request.POST["fst_name_aluno"],
                                        alu_segundo_nome = request.POST["scn_name_aluno"],
                                        alu_data_nascimento = datetime.datetime.strptime(str(request.POST["date_nasc_aluno"]),'%d/%m/%Y').strftime('%Y-%m-%d'),
                                        turma = core.models.Turma(tur_id = request.POST["turma"]),
                                        tipo = core.models.TipoAluno(tip_alu_id = request.POST["tipo"]))
    

    response = redirect('/gestor/alunos', context)

    return response

def delete_alunos(request,id):
    context = {
        'segment': 'alunos',
        'err':''
    }

    aluno = core.models.Aluno.objects.get(alu_id = id)
    aluno.delete()

    response = redirect('/gestor/alunos', context)

    return response

#Escolas
def submit_escola(request):
    context = {
        'segment': 'escolas',
        'err':''
    }

    # data = request.POST
    identificador = request.COOKIES.get('identificador_gestor')

    nome_escola = request.POST["nome_escola"]
    codigo_inep = request.POST["codigo_inep"]
    categoria = request.POST["categoria"]
    dependencia = request.POST["dependencia"]
    uf = request.POST["uf"]
    cep = request.POST["cep"]
    municipio = request.POST["municipio"]
    endereco = request.POST["endereco"]

    scripts_mongodb = ScriptsMongoDB()

    gestor_query = scripts_mongodb.get_data_find(
        collection_name='gestores',
        filter = {'identificador': identificador}
    )[0]

    escolas = gestor_query["escolas"]

    result = scripts_mongodb.insert_object(
        collection_name="escolas",
        object={
            "nome": nome_escola,
            "codigo_inep": codigo_inep,
            "categ_admin": int(categoria),
            "depen_admin": int(dependencia),
            "uf": uf,
            "cep": cep,
            "municipio": municipio,
            "endereco": endereco,
            "hash_senha": "",
            "infraestruturas": [],
            "turmas": []
        }
    )

    # teste = {}[0]
    escolas.append(ObjectId(result["id"]))

    scripts_mongodb.db["gestores"].update_one({"_id": gestor_query["_id"]}, {"$set": {"escolas": escolas}})

    scripts_mongodb.close_connection()

    response = redirect('/gestor/escolas', context)
    response.set_cookie('identificador_gestor', identificador)

    return response

def escola_individual(request,id):
    identificador = request.COOKIES.get('identificador_gestor')

    escola = core.models.UnidadeEscolar.objects.filter(uni_id = id).select_related('endereco')[0]
    turmas = core.models.Turma.objects.filter(escola_id = id).select_related('professor')

    context={
        "escola": escola,
        "turmas":turmas
    }

    html_template = loader.get_template('gestor/screens/escola_individual.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def escolas(request):

    identificador = request.COOKIES.get('identificador_gestor')

    gestor = core.models.GestorEscola.objects.get(ges_identificador = identificador)

    #escolas = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id).select_related()

    #escolas_federais = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id,tipo_id = 1).select_related()

    #escolas_estaduais = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id,tipo_id = 2).select_related()
    
    #escolas_municipais = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id,tipo_id = 3).select_related()

    escolas = core.models.UnidadeEscolar.objects.all().select_related()

    escolas_federais = core.models.UnidadeEscolar.objects.filter(tipo_id = 1).select_related()

    escolas_estaduais = core.models.UnidadeEscolar.objects.filter(tipo_id = 2).select_related()
    
    escolas_municipais = core.models.UnidadeEscolar.objects.filter(tipo_id = 3).select_related()

    print(str(escolas.query))

    context = {
        'segment': 'escolas',
        'escolas_federais': escolas_federais,
        'escolas_estaduais': escolas_estaduais,
        'escolas_municipais': escolas_municipais,
        'escolas': escolas,
    }

    html_template = loader.get_template('gestor/screens/escolas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def cadastro_escolas(request):
    identificador = request.COOKIES.get('identificador_gestor')

    context={}

    html_template = loader.get_template('gestor/screens/cadastro_escolas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

#Turma
def cadastro_turma(request):
    identificador = request.COOKIES.get('identificador_gestor')
    id_escola = request.COOKIES.get('id_escola')

    context={}

    html_template = loader.get_template('gestor/screens/cadastro_turma.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)
    response.set_cookie('id_escola', id_escola)

    return response

def submit_turma(request):
    context = {
        'segment': 'escolas',
        'err':''
    }

    # data = request.POST
    identificador = request.COOKIES.get('identificador_gestor')
    id_escola = request.COOKIES.get('id_escola')

    ano = request.POST["ano"]
    nome_provedor = request.POST["nome_provedor"]
    ano_escolar = request.POST["ano_escolar"]

    scripts_mongodb = ScriptsMongoDB()

    escola_query = scripts_mongodb.get_object_by_id(
        collection_name='escolas',
        _id=id_escola
    )

    turmas = escola_query["turmas"]

    result = scripts_mongodb.insert_object(
        collection_name="turmas",
        object={
            "ano":ano,
            "nome_provedor":nome_provedor,
            "ano_escolar":ano_escolar,
            "alunos":[],
            "professor":None
        }
    )

    turmas.append(ObjectId(result["id"]))
    # teste = {}[0]

    scripts_mongodb.db["escolas"].update_one({"_id": ObjectId(id_escola)}, {"$set": {"turmas": turmas}})

    scripts_mongodb.close_connection()

    response = redirect('/gestor/escola_individual', context)
    response.set_cookie('identificador_gestor', identificador)

    return response

#Geral
def gestores_escolares(request):
    identificador = request.COOKIES.get('identificador_gestor')

    # gestor = core.models.GestorEscola.objects.get(ges_identificador = identificador)

    # professores = core.models.Professor.objects.raw("SELECT p.pro_id, p.pro_primeiro_nome, "+
    # "p.pro_segundo_nome, string_agg(CONCAT('Ano: ',tur_ano,' Serie: ', tur_ano_escolar), ', ') AS turmas "+
    # "FROM professor AS p LEFT JOIN turma AS t ON t.pro_id = p.pro_id GROUP BY p.pro_id ORDER BY p.pro_id");

    # # scripts_mongodb = ScriptsMongoDB()

    # # escolas_query = scripts_mongodb.get_data_find(
    # #     collection_name='gestores',
    # #     filter = {'identificador': identificador}
    # # )[0]['escolas']

    # # aux_escolas = []

    # # escolas = []
    # # labels_chart = []
    # # data_chart = []
    # # total_turmas = 0

    # # for escola in escolas_query:
    # #     escola_query = scripts_mongodb.get_object_by_id(
    # #         collection_name='escolas',
    # #         _id=escola
    # #     )
    # #     aux_escolas.append(escola_query)

    # # for escola in aux_escolas:
    # #     labels_chart.append(escola["nome"])
    # #     data_chart.append(len(escola["turmas"]))
    # #     escolas.append({
    # #         "nome": escola["nome"],
    # #         "quantidade": len(escola["turmas"])
    # #     })
    # #     total_turmas += len(escola["turmas"])

    # # scripts_mongodb.close_connection()

    # context = {
    #     'segment': 'gestores_escolares',
    #     'escolas': escolas,
    #     'total_turmas': total_turmas,
    #     'labels_chart': labels_chart[:5],
    #     'data_chart': data_chart[:5]
    # }

    context = {
        'segment': 'gestores_escolares',
    }

    html_template = loader.get_template('gestor/screens/gestores_escolares.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def resumo_coletas(request):
    identificador = request.COOKIES.get('identificador_gestor')

    # scripts_mongodb = ScriptsMongoDB()

    # escolas_query = scripts_mongodb.get_data_find(
    #     collection_name='gestores',
    #     filter = {'identificador': identificador}
    # )[0]['escolas']

    # list_alunos = []
    # escolas = []

    # for escola_id in escolas_query:

    #     escola = scripts_mongodb.get_object_by_id(
    #         collection_name='escolas',
    #         _id=escola_id
    #     )
    #     escola_aux = {"nome": escola["nome"], "alunos": []}
    #     for turma_id in escola["turmas"]:
    #         turma = scripts_mongodb.get_object_by_id(
    #             collection_name='turmas',
    #             _id=turma_id
    #         )
    #         escola_aux['alunos'] = escola_aux['alunos'] + turma["alunos"]
    #         list_alunos = list_alunos + turma["alunos"]
    #     escolas.append(escola_aux)

    # avaliacoes = {}

    # for aluno in list_alunos:
    #     avaliacoes[aluno] = scripts_mongodb.get_data_find(
    #             collection_name='alunos',
    #             filter = {'_id': aluno}
    #         )[0]["avaliacao"]

    # list_avaliacoes = {}
    # for key in avaliacoes:
    #     list_avaliacoes[avaliacoes[key]] = scripts_mongodb.get_data_find(
    #             collection_name='avaliacoes',
    #             filter = {'_id': avaliacoes[key]}
    #         )[0]
    # scripts_mongodb.close_connection()

    # escolas_name_label = []
    # mean_av1 = []
    # mean_av2 = []
    # mean_av3 = []

    # for escola in escolas:
    #     escolas_name_label.append(escola["nome"])
    #     av1 = 0
    #     cont1 = 0
    #     av2 = 0
    #     cont2 = 0
    #     av3 = 0
    #     cont3 = 0
    #     for aluno in escola["alunos"]:
    #         avaliacao_id = avaliacoes[aluno]
    #         avaliacao = list_avaliacoes[avaliacao_id]["avaliacoes"]
    #         for coleta in avaliacao[0]["coleta"]:
    #             if(coleta["metrica"] != None):
    #                 av1 += coleta["metrica"]
    #                 cont1 += 1
    #         for coleta in avaliacao[1]["coleta"]:
    #             if(coleta["metrica"] != None):
    #                 av2 += coleta["metrica"]
    #                 cont2 += 1
    #         for coleta in avaliacao[2]["coleta"]:
    #             if(coleta["metrica"] != None):
    #                 av3 += coleta["metrica"]
    #                 cont3 += 1

    #     if cont1 != 0:
    #         mean_av1.append(av1/cont1)
    #     else:
    #         mean_av1.append(0)
    #     if cont2 != 0:
    #         mean_av2.append(av2/cont2)
    #     else:
    #         mean_av2.append(0)
    #     if cont3 != 0:
    #         mean_av3.append(av3/cont3)
    #     else:
    #         mean_av3.append(0)
    #     # teste={}[0]

    # context = {
    #     'segment': 'resumo_coletas',
    #     'avaliacoes': list_avaliacoes,
    #     "escolas_name_label":   escolas_name_label,
    #     "mean_av1": mean_av1,
    #     "mean_av2": mean_av2,
    #     "mean_av3": mean_av3
    # }
    context = {
        'segment': 'gestores_escolares',
    }
    html_template = loader.get_template('gestor/screens/resumo_coletas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

