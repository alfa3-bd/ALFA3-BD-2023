from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from utils.CryptoHelper import CryptoHelper
from random import randint
from utils.CryptoHelper import CryptoHelper
import core.models
import os

def login(request):
    context = {
        'segment': 'login'
    }
    html_template = loader.get_template('professor/screens/login.html')
    return HttpResponse(html_template.render(context, request))

def logoff(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('identificador_professor')

    return response

def verify_login(request):

    crypto = CryptoHelper()

    context = {
        'segment': 'login',
        'err':''
    }

    if len(request.POST['identificador_professor']):

        data = request.POST
        professor = core.models.Professor.objects.get(pro_identificador = data['identificador_professor'])

        if len(professor.pro_identificador) and (crypto.decrypt_message(professor.pro_senha) == data['senha_professor']):

            context = {
                'segment': 'home',
                'err':''
            }

            response = redirect('/professor/home', context)
            response.set_cookie('identificador_professor', professor.pro_identificador)
            return response

    return redirect('/professor/login', context)

def home(request):
    context = {
        'segment': 'home'
    }

    identificador = request.COOKIES.get('identificador_professor')

    if identificador is not None:

        html_template = loader.get_template('professor/screens/home.html')

        response = HttpResponse(html_template.render(context, request))
        response.set_cookie('identificador_professor', identificador)

        return HttpResponse(html_template.render(context, request))

    else:
        context = {
            'segment': 'login',
            'err':''
        }

        return redirect('/professor/login', context)

def informacoes(request):

    identificador = request.COOKIES.get('identificador_professor')

    if not identificador:
        return redirect('/professor/login')

    professor = core.models.Professor.objects.get(pro_identificador = identificador)

    context = {
        'segment': 'informacoes',
        'professor': professor,
    }

    html_template = loader.get_template('professor/screens/informacoes.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_professor', identificador)

    return response

def coleta(request,id):

    identificador = request.COOKIES.get('identificador_professor')

    if not identificador:
        return redirect('/professor/login')

    aluno = core.models.Aluno.objects.raw("SELECT al.alu_id, al.alu_primeiro_nome, al.alu_segundo_nome, "+
                                              "pr.pro_id, pr.pro_primeiro_nome, pr.pro_segundo_nome "+
                                              "FROM aluno AS al "+
                                              "JOIN turma AS tr ON tr.tur_id = al.tur_id "+
                                              "JOIN professor AS pr ON pr.pro_id = tr.tur_id "+
                                              "WHERE al.alu_id = '"+str(id)+"' ")[0];
    
    frases_tipo_1 = core.models.Frase.objects.filter(tipo_id = 1).select_related('tipo')
    frases_tipo_2 = core.models.Frase.objects.filter(tipo_id = 2).select_related('tipo')
    frases_tipo_3 = core.models.Frase.objects.filter(tipo_id = 3).select_related('tipo')

    frases = {
        'tipo_1': frases_tipo_1[randint(0, len(frases_tipo_1)-1)],
        'tipo_2': frases_tipo_2[randint(0, len(frases_tipo_2)-1)],
        'tipo_3': frases_tipo_3[randint(0, len(frases_tipo_3)-1)],
    }

    context = {
        'segment': 'coleta',
        'aluno': aluno,
        'frases': frases
    }


    html_template = loader.get_template('professor/screens/coleta.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_professor', identificador)

    return response

def view_audio_metrics(request,id):

    identificador = request.COOKIES.get('identificador_professor')

    if not identificador:
        return redirect('/professor/login')

    aluno = core.models.Aluno.objects.raw("SELECT al.alu_id, al.alu_primeiro_nome, al.alu_segundo_nome, "+
                                              "pr.pro_id, pr.pro_primeiro_nome, pr.pro_segundo_nome "+
                                              "FROM aluno AS al "+
                                              "JOIN turma AS tr ON tr.tur_id = al.tur_id "+
                                              "JOIN professor AS pr ON pr.pro_id = tr.tur_id "+
                                              "WHERE al.alu_id = '"+str(id)+"' ")[0];
    
    avaliacoes = core.models.Avaliacao.objects.raw("SELECT al.ava_id, al.ava_data, al.ava_nota, ta.tip_aval_desc, "+
                                                   "fr.fra_frase, tf.tip_frase_desc "+
                                                   "FROM coleta AS cl "+
                                                   "JOIN avaliacao AS al ON cl.ava_id = al.ava_id "+
                                                   "JOIN tipo_avaliacao AS ta ON ta.tip_aval_id = al.ava_tipo "+
                                                   "JOIN frase AS fr ON fr.fra_id = cl.fra_id "+
                                                   "JOIN tipo_frase AS tf ON tf.tip_frase_id = fr.tip_frase "+ 
                                                   "WHERE al.alu_id = '"+str(id)+"' "+                            
                                                   "ORDER BY ta.tip_aval_desc ");
        
    context = {
        'segment': 'coleta',
        'aluno': aluno,
        'aval_count':len(avaliacoes),
        'avaliacoes': avaliacoes
    }

    html_template = loader.get_template('professor/screens/audio_metrics.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_gestor', identificador)

    return response

def getAudio(request):
    if request.method == "POST":
        if request.FILES.get("myAudio", False):
            handleUploadFile(request.FILES["myAudio"])
    return HttpResponse()

def handleUploadFile(f):  
    with open("C:/Temp/" + f.name, "wb+") as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

def submit_audios(request):

    crypto = CryptoHelper()

    context = {
        'segment': 'turmas',
        'err':''
    }

    identificador = request.COOKIES.get('identificador_professor')

    if request.method == "POST":
        if not os.path.isdir("C:/Temp"):
            os.makedirs("C:/Temp")

        for i in range(1,4):
            f = "file{0}".format(i)
            if request.FILES.get(f, False):
                files = request.FILES[f]
                with open("C:/Temp/" + files.name, "wb+") as destination:  
                    for chunk in files.chunks():  
                        destination.write(chunk)
        
        aluno_id = request.POST["aluno_id"]
        frase1 = request.POST["frase1"]
        frase2 = request.POST["frase2"]
        frase3 = request.POST["frase3"]
        
    response = redirect('/professor/turmas', context)
    response.set_cookie('identificador_professor', identificador)

    return response

def banco_frases(request):

    identificador = request.COOKIES.get('identificador_professor')

    if not identificador:
        return redirect('/professor/login')
    
    frases = core.models.Frase.objects.all().select_related().order_by('fra_id')

    print(frases[0].tipo.tip_frase_id)
    context = {
        'segment': 'banco_frases',
        'frases': frases
    }

    html_template = loader.get_template('professor/screens/banco_frases.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_professor', identificador)

    return response

def turmas(request):

    identificador = request.COOKIES.get('identificador_professor')

    if not identificador:
        return redirect('/professor/login')

    turmas = core.models.Turma.objects.raw("SELECT tr.tur_id, tr.tur_ano, tr.tur_ano_escolar, COUNT(al.*) AS turma_qtd "+
                                            "FROM turma AS tr "+
                                            "JOIN professor AS pr ON tr.pro_id = pr.pro_id "+
                                            "LEFT JOIN aluno AS al ON al.tur_id = tr.tur_id "+ 
                                            "WHERE pr.pro_identificador = '"+identificador+"' "+
                                            "GROUP BY tr.tur_id, tr.tur_ano, tr.tur_ano_escolar "+
                                            "ORDER BY tr.tur_ano DESC, tr.tur_ano_escolar");


    context = {
        'segment': 'turmas',
        'turmas': turmas
    }

    html_template = loader.get_template('professor/screens/turmas.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_professor', identificador)
    return response

def alunos(request,id):

    identificador = request.COOKIES.get('identificador_professor')

    if not identificador:
        return redirect('/professor/login')

    alunos = core.models.Aluno.objects.filter(turma=id).select_related('turma').order_by('alu_primeiro_nome')

    context = {
        'segment': 'alunos',
        'alunos': alunos
    }

    html_template = loader.get_template('professor/screens/alunos.html')
    response = HttpResponse(html_template.render(context, request))
    response.set_cookie('identificador_professor', identificador)

    return response

