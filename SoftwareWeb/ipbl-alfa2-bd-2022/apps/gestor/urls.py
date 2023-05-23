from django.urls import path, re_path
from apps.gestor import views

urlpatterns = [
    path('login', views.login, name='gestor'),
    path('verify_login', views.verify_login, name='gestor'),
    path('logoff', views.logoff, name='gestor'),

    path('home', views.home, name='gestor'),
    path('informacoes', views.informacoes, name='gestor'),
    
    path('professores', views.professores, name='gestor'),
    path('add_professores', views.add_professores, name='gestor'),
    path('save_professores', views.save_professores, name='gestor'),
    path('edit_professores/<int:id>', views.edit_professores, name='gestor'),
    path('delete_professores/<int:id>', views.delete_professores, name='gestor'),

    path('alunos', views.alunos, name='gestor'),
    path('add_alunos', views.add_alunos, name='gestor'),
    path('save_alunos', views.save_alunos, name='gestor'),
    path('edit_alunos/<int:id>', views.edit_alunos, name='gestor'),
    path('delete_alunos/<int:id>', views.delete_alunos, name='gestor'),

    path('gestores_escolares', views.gestores_escolares, name='gestor'),
    path('resumo_coletas', views.resumo_coletas, name='gestor'),

    path('escolas', views.escolas, name='gestor'),
    path('cadastro_escolas', views.cadastro_escolas, name='gestor'),
    path('submit_escola', views.submit_escola, name='gestor'),
    path('escola_individual/<int:id>', views.escola_individual, name='gestor'),

    path('cadastro_turma', views.cadastro_turma, name='gestor'),
    path('submit_turma', views.submit_turma, name='gestor'),

]
