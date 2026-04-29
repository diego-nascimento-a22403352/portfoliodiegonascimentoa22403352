from django.shortcuts import render, redirect
from .models import Projeto, TFC, Tecnologia, Licenciatura, UnidadeCurricular, Competencia
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, LicenciaturaForm

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

def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()

    return render(request, 'portfolio/novo_projeto.html', {'form': form})

def editar_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/editar_projeto.html', {'form': form, 'projeto': projeto})

def apagar_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
        
    return render(request, 'portfolio/apagar_projeto.html', {'projeto': projeto})


from .forms import TecnologiaForm, CompetenciaForm, LicenciaturaForm
from .models import Tecnologia, Competencia, Licenciatura

# ==========================================
# VIEWS PARA TECNOLOGIAS
# ==========================================
def nova_tecnologia_view(request):
    if request.method == 'POST':
        # O request.FILES é obrigatório porque a tecnologia tem um ImageField
        form = TecnologiaForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/form_tecnologia.html', {'form': form, 'acao': 'Adicionar'})

def editar_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/form_tecnologia.html', {'form': form, 'acao': 'Editar', 'tecnologia': tecnologia})

def apagar_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/apagar_generico.html', {'item': tecnologia, 'tipo': 'Tecnologia', 'url_cancelar': 'tecnologias'})

# ==========================================
# VIEWS PARA COMPETÊNCIAS
# ==========================================
def nova_competencia_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/form_competencia.html', {'form': form, 'acao': 'Adicionar'})

def editar_competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/form_competencia.html', {'form': form, 'acao': 'Editar'})

def apagar_competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/apagar_generico.html', {'item': competencia, 'tipo': 'Competência', 'url_cancelar': 'competencias'})

# ==========================================
# VIEWS PARA LICENCIATURAS (FORMAÇÃO)
# ==========================================
def nova_licenciatura_view(request):
    if request.method == 'POST':
        form = LicenciaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('licenciaturas')
    else:
        form = LicenciaturaForm()
    return render(request, 'portfolio/form_licenciatura.html', {'form': form, 'acao': 'Adicionar'})

def editar_licenciatura_view(request, id):
    licenciatura = Licenciatura.objects.get(id=id)
    if request.method == 'POST':
        form = LicenciaturaForm(request.POST, instance=licenciatura)
        if form.is_valid():
            form.save()
            return redirect('licenciaturas')
    else:
        form = LicenciaturaForm(instance=licenciatura)
    return render(request, 'portfolio/form_licenciatura.html', {'form': form, 'acao': 'Editar'})

def apagar_licenciatura_view(request, id):
    licenciatura = Licenciatura.objects.get(id=id)
    if request.method == 'POST':
        licenciatura.delete()
        return redirect('licenciaturas')
    return render(request, 'portfolio/apagar_generico.html', {'item': licenciatura, 'tipo': 'Licenciatura', 'url_cancelar': 'licenciaturas'})

import os
from django.conf import settings

def sobre_view(request):
    # Caminho para o teu ficheiro .md na raiz do projeto
    caminho_ficheiro = os.path.join(settings.BASE_DIR, 'MAKING_OF.md')
    
    try:
        with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
            conteudo_markdown = f.read()
    except FileNotFoundError:
        conteudo_markdown = "O ficheiro MAKING_OF.md não foi encontrado."

    return render(request, 'portfolio/sobre.html', {'making_of': conteudo_markdown})