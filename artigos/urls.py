from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('novo/', views.novo_artigo_view, name='novo_artigo'),
    path('<int:id>/', views.artigo_detalhe_view, name='artigo_detalhe'),
    path('<int:id>/editar/', views.editar_artigo_view, name='editar_artigo'),
    path('<int:id>/apagar/', views.apagar_artigo_view, name='apagar_artigo'),
    path('<int:id>/like/', views.like_artigo_view, name='like_artigo'),
]