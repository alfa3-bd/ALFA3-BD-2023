from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from utils.CryptoHelper import CryptoHelper
import datetime
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

    if not identificador:
        return redirect('/gestor/login')

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

    if not identificador:
        return redirect('/gestor/login')

    professores = core.models.Professor.objects.raw("SELECT p.pro_id, p.pro_primeiro_nome, p.pro_segundo_nome, "+
                                                    "string_agg(CONCAT(tur_ano_escolar,'º - ',tur_ano), ' , ') AS turmas "+
                                                    "FROM professor AS p "+
                                                    "LEFT JOIN turma AS t ON t.pro_id = p.pro_id "+
                                                    "GROUP BY p.pro_id ORDER BY p.pro_id");

    context = {
        'segment': 'professores',
        'professores': professores,
    }

    html_template = loader.get_template('gestor/screens/professores.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def add_professores(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    context = {
        'segment': 'professores',
        'err':''
    }
     
    html_template = loader.get_template('gestor/screens/add_professores.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def edit_professores(request,id):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    crypto = CryptoHelper()
    professor = core.models.Professor.objects.get(pro_id = id)
    professor.pro_senha = crypto.decrypt_message(professor.pro_senha)

    context = {
        'segment': 'professores',
        'professor': professor,
    }

    html_template = loader.get_template('gestor/screens/edit_professores.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def save_professores(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

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
    response.set_cookie('identificador_gestor', identificador)

    return response

def delete_professores(request,id):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')
    
    context = {
        'segment': 'professores',
        'err':''
    }

    professor = core.models.Professor.objects.get(pro_id = id)
    professor.delete()

    response = redirect('/gestor/professores', context)
    response.set_cookie('identificador_gestor', identificador)

    return response

# Alunos
def alunos(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')
    
    alunos = core.models.Aluno.objects.raw("SELECT * from view_alunos "+
                                            "WHERE ges_identificador = '"+identificador+"' "+
                                            "ORDER BY alu_primeiro_nome");

    context = {
        'segment': 'alunos',
        'alunos': alunos,
    }

    html_template = loader.get_template('gestor/screens/alunos.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def add_alunos(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    tipo_alunos = core.models.TipoAluno.objects.all()
    turmas = core.models.Turma.objects.raw("SELECT tr.tur_id,tr.tur_ano,tr.tur_ano_escolar, ue.uni_nome "+
                                            "FROM turma AS tr "+
                                            "JOIN unidade_escolar AS ue ON ue.uni_id = tr.uni_id "+
                                            "JOIN gestor_escola AS ge ON ge.ges_id = tr.uni_id "+
                                            "WHERE ge.ges_identificador = '"+identificador+"' "+
                                            "ORDER BY tr.tur_ano,tr.tur_ano_escolar DESC");
    

    context = {
        'segment': 'alunos',
        'turmas':turmas,
        'tipo_alunos':tipo_alunos,
    }

    html_template = loader.get_template('gestor/screens/add_alunos.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def edit_alunos(request,id):
    
    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

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
    response.set_cookie('identificador_gestor', identificador)

    return response

def save_alunos(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    context = {
        'segment': 'alunos',
        'err':''
    }

    if 'id_aluno' in request.POST:
        aluno = core.models.Aluno.objects.get(alu_id = request.POST["id_aluno"])
        aluno.alu_primeiro_nome=request.POST["fst_name_aluno"]
        aluno.alu_segundo_nome = request.POST["scn_name_aluno"]
        aluno.alu_data_nascimento = datetime.datetime.strptime(str(request.POST["date_nasc_aluno"]),'%d/%m/%Y').strftime('%Y-%m-%d')
        aluno.turma = core.models.Turma.objects.get(tur_id = request.POST["turma"])
        aluno.tipo = core.models.TipoAluno.objects.get(tip_alu_id = request.POST["tipo"])
        aluno.save()
    
    else:
        core.models.Aluno.objects.create(alu_primeiro_nome=request.POST["fst_name_aluno"],
                                        alu_segundo_nome = request.POST["scn_name_aluno"],
                                        alu_data_nascimento = datetime.datetime.strptime(str(request.POST["date_nasc_aluno"]),'%d/%m/%Y').strftime('%Y-%m-%d'),
                                        turma = core.models.Turma.objects.get(tur_id = request.POST["turma"]),
                                        tipo = core.models.TipoAluno.objects.get(tip_alu_id = request.POST["tipo"]))
    

    response = redirect('/gestor/alunos', context)
    response.set_cookie('identificador_gestor', identificador)

    return response

def delete_alunos(request,id):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')
    
    context = {
        'segment': 'alunos',
        'err':''
    }

    aluno = core.models.Aluno.objects.get(alu_id = id)
    aluno.delete()

    response = redirect('/gestor/alunos', context)
    response.set_cookie('identificador_gestor', identificador)

    return response

#Escolas
def escola_individual(request,id):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

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

    if not identificador:
        return redirect('/gestor/login')

    gestor = core.models.GestorEscola.objects.get(ges_identificador = identificador)

    escolas = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id).select_related()

    escolas_federais = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id,tipo_id = 1).select_related()

    escolas_estaduais = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id,tipo_id = 2).select_related()
    
    escolas_municipais = core.models.UnidadeEscolar.objects.filter(gestor_id = gestor.ges_id,tipo_id = 3).select_related()

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

def add_escolas(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    categorias = core.models.CategoriaEscolar.objects.all()
    tipos_escola = core.models.TipoEscola.objects.all()
    cidades = core.models.Cidade.objects.all()

    context = {
        "categorias":categorias,
        "tipos":tipos_escola,
        "cidades":cidades
    }

    html_template = loader.get_template('gestor/screens/add_escolas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

@transaction.atomic
def save_escola(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    #get identity
    new_cidade = core.models.Endereco.objects.create(end_rua = request.POST["rua"],
                                        end_numero = request.POST["numero"],
                                        end_cep = request.POST["cep"],
                                        cidade = core.models.Cidade.objects.get(cid_id = request.POST["municipio"]))
    
    core.models.UnidadeEscolar.objects.create(uni_codigo_inep = request.POST["codigo_inep"],
                                        uni_nome = request.POST["nome_escola"],
                                        categoria = core.models.CategoriaEscolar.objects.get(cat_escola_id = request.POST["categoria"]),
                                        tipo = core.models.TipoEscola.objects.get(tip_escola_id = request.POST["tipo_escola"]),
                                        gestor = core.models.GestorEscola.objects.get(ges_identificador = identificador),
                                        endereco = core.models.Endereco.objects.get(end_id = new_cidade.end_id))

    context = {
        'segment': 'escolas',
        'err':''
    }

    response = redirect('/gestor/escolas', context)
    response.set_cookie('identificador_gestor', identificador)

    return response

#Turma
def add_turma(request,id):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    professores = core.models.Professor.objects.all().order_by('pro_primeiro_nome')

    context = {
        "professores":professores,
        "escola":id
    }

    html_template = loader.get_template('gestor/screens/add_turma.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def save_turma(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    context = {
        'segment': 'escolas',
        'err':''
    }
    
    unidade_escolar = request.POST["uni_id"]

    core.models.Turma.objects.create(tur_ano = request.POST["ano"],
                                     tur_ano_escolar = request.POST["ano_escolar"],
                                     escola = core.models.UnidadeEscolar.objects.get(uni_id = unidade_escolar),
                                     professor = core.models.Professor.objects.get(pro_id = request.POST["provedor"]))
    
    response = redirect('/gestor/escola_individual/'+unidade_escolar, context)
    response.set_cookie('identificador_gestor', identificador)

    return response

#Geral
def gestores_escolares(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')

    escolas_q = core.models.UnidadeEscolar.objects.raw("SELECT ue.uni_id, ue.uni_nome, COUNT(*) AS ct_turmas "+
                                                        "FROM unidade_escolar AS ue "+
                                                        "JOIN gestor_escola AS ge ON ge.ges_id =  ue.ges_id "+
                                                        "JOIN turma AS tr ON tr.uni_id = ue.uni_id "+ 
                                                        "WHERE ge.ges_identificador = '"+identificador+"' GROUP BY ue.uni_id");

    escolas = []
    labels_chart = []
    data_chart = []
    total_turmas = 0

    for escola in escolas_q:
        labels_chart.append(escola.uni_nome)
        data_chart.append(escola.ct_turmas)
        escolas.append({
            "nome": escola.uni_nome,
            "quantidade": escola.ct_turmas
        })
        total_turmas += escola.ct_turmas
        
    context = {
        'segment': 'gestores_escolares',
        'escolas': escolas,
        'total_turmas': total_turmas,
        'labels_chart': labels_chart,
        'data_chart': data_chart
    }

    html_template = loader.get_template('gestor/screens/gestores_escolares.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def resumo_coletas(request):

    identificador = request.COOKIES.get('identificador_gestor')

    if not identificador:
        return redirect('/gestor/login')
    
    escolas_q = core.models.UnidadeEscolar.objects.raw("SELECT ue.uni_id,av.ava_tipo, AVG(COALESCE(ava_nota,0)) AS avg_nota "+
                                                        "FROM unidade_escolar AS ue "+
                                                        "JOIN gestor_escola AS ge ON ge.ges_id = ue.ges_id "+
                                                        "JOIN turma AS tr ON tr.uni_id = ue.uni_id "+
                                                        "JOIN aluno AS al ON al.tur_id = tr.tur_id "+
                                                        "JOIN avaliacao AS av ON av.alu_id = al.alu_id "+
                                                        "WHERE ge.ges_identificador = '"+identificador+"' "+
                                                        "GROUP BY ue.uni_id,ue.uni_nome,av.ava_tipo ORDER BY ue.uni_nome,av.ava_tipo");

    escolas_name_label = []
    mean_av1 = []
    mean_av2 = []
    mean_av3 = []
    i = -1

    for escola in escolas_q:
        if(escola.uni_nome not in escolas_name_label):
            escolas_name_label.append(escola.uni_nome)
            mean_av1.append(0)
            mean_av2.append(0)
            mean_av3.append(0)
            i += 1
        
        if escola.ava_tipo == 1:
            mean_av1[i] = round(escola.avg_nota)
        elif escola.ava_tipo == 2:
            mean_av2[i] = round(escola.avg_nota)
        elif escola.ava_tipo == 3:
            mean_av3[i] = round(escola.avg_nota)


    context = {
        'segment': 'resumo_coletas',
        "escolas_name_label":   escolas_name_label,
        "mean_av1": mean_av1,
        "mean_av2": mean_av2,
        "mean_av3": mean_av3
    }


    html_template = loader.get_template('gestor/screens/resumo_coletas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

