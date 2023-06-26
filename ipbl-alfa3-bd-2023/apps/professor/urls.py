from django.urls import path, re_path
from apps.professor import views

urlpatterns = [

    # The home page
    path('login', views.login, name='professor'),
    path('verify_login', views.verify_login, name='professor'),
    path('logoff', views.logoff, name='professor'),

    path('home', views.home, name='professor'),
    path('informacoes', views.informacoes, name='professor'),

    path('turmas', views.turmas, name='professor'),
    path('alunos/<int:id>', views.alunos, name='professor'),

    path('coleta/<int:id>', views.coleta, name='professor'),
    path('refazer_coleta/<int:id>', views.refazer_coleta, name='professor'),
    path('submit_audios', views.submit_audios, name='professor'),

    path('banco_frases', views.banco_frases, name='professor'),
    path('view_audio_metrics/<int:id>', views.view_audio_metrics, name='professor'),
]
