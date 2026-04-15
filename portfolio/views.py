from django.shortcuts import render
from .models import Projeto, TFC, Tecnologia, Licenciatura, UnidadeCurricular, Competencia

def projetos_view(request):
    # Usamos prefetch_related porque um projeto tem várias tecnologias/competências
    projetos = Projeto.objects.prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def ucs_view(request):
    # Usamos select_related porque cada UC pertence a 1 licenciatura (mais eficiente!)
    ucs = UnidadeCurricular.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def competencias_view(request):
    # prefetch_related para ir buscar os projetos associados a cada competência
    competencias = Competencia.objects.prefetch_related('projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})