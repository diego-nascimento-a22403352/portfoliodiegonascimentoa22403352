from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.projetos_view, name='projetos'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('competencias/', views.competencias_view, name='competencias'),
    
    path('', views.projetos_view, name='home_portfolio'),
]