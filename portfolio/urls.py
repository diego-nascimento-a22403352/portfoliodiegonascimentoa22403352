from django.urls import path
from . import views

urlpatterns = [
    # Rota principal do portefólio
    path('', views.projetos_view, name='home_portfolio'),
    
    # ==========================================
    # ROTAS DE LISTAGEM (O que já tinhas)
    # ==========================================
    path('projetos/', views.projetos_view, name='projetos'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('competencias/', views.competencias_view, name='competencias'),
    
    # ==========================================
    # ROTAS CRUD - PROJETOS
    # ==========================================
    path('projetos/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projetos/<int:id>/editar/', views.editar_projeto_view, name='editar_projeto'),
    path('projetos/<int:id>/apagar/', views.apagar_projeto_view, name='apagar_projeto'),

    # ==========================================
    # ROTAS CRUD - TECNOLOGIAS
    # ==========================================
    path('tecnologias/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologias/<int:id>/editar/', views.editar_tecnologia_view, name='editar_tecnologia'),
    path('tecnologias/<int:id>/apagar/', views.apagar_tecnologia_view, name='apagar_tecnologia'),

    # ==========================================
    # ROTAS CRUD - COMPETÊNCIAS
    # ==========================================
    path('competencias/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencias/<int:id>/editar/', views.editar_competencia_view, name='editar_competencia'),
    path('competencias/<int:id>/apagar/', views.apagar_competencia_view, name='apagar_competencia'),

    # ==========================================
    # ROTAS CRUD - LICENCIATURAS (Formação)
    # ==========================================
    path('licenciaturas/nova/', views.nova_licenciatura_view, name='nova_licenciatura'),
    path('licenciaturas/<int:id>/editar/', views.editar_licenciatura_view, name='editar_licenciatura'),
    path('licenciaturas/<int:id>/apagar/', views.apagar_licenciatura_view, name='apagar_licenciatura'),


    path('sobre/', views.sobre_view, name='sobre'),
]