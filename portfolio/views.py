from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Projeto, TFC, Tecnologia, Licenciatura, UnidadeCurricular, Competencia
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, LicenciaturaForm
import os
from django.conf import settings

# ==========================================
# VIEWS DE LISTAGEM (Públicas)
# ==========================================

def projetos_view(request):
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
    ucs = UnidadeCurricular.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def sobre_view(request):
    caminho_ficheiro = os.path.join(settings.BASE_DIR, 'MAKING_OF.md')
    try:
        with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
            conteudo_markdown = f.read()
    except FileNotFoundError:
        conteudo_markdown = "O ficheiro MAKING_OF.md não foi encontrado."
    return render(request, 'portfolio/sobre.html', {'making_of': conteudo_markdown})

# ==========================================
# OPERAÇÕES CRUD (Protegidas)
# ==========================================

# Função auxiliar para verificar se o utilizador é Gestor de Portfólio
def e_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()

# --- PROJETOS ---
@login_required
def novo_projeto_view(request):
    if not e_gestor(request.user):
        return redirect('projetos')
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

@login_required
def editar_projeto_view(request, id):
    if not e_gestor(request.user):
        return redirect('projetos')
    projeto = Projeto.objects.get(id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/editar_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def apagar_projeto_view(request, id):
    if not e_gestor(request.user):
        return redirect('projetos')
    projeto = Projeto.objects.get(id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/apagar_projeto.html', {'projeto': projeto})

# --- TECNOLOGIAS ---
@login_required
def nova_tecnologia_view(request):
    if not e_gestor(request.user):
        return redirect('tecnologias')
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/form_tecnologia.html', {'form': form, 'acao': 'Adicionar'})

@login_required
def editar_tecnologia_view(request, id):
    if not e_gestor(request.user):
        return redirect('tecnologias')
    tecnologia = Tecnologia.objects.get(id=id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/form_tecnologia.html', {'form': form, 'acao': 'Editar', 'tecnologia': tecnologia})

@login_required
def apagar_tecnologia_view(request, id):
    if not e_gestor(request.user):
        return redirect('tecnologias')
    tecnologia = Tecnologia.objects.get(id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/apagar_generico.html', {'item': tecnologia, 'tipo': 'Tecnologia', 'url_cancelar': 'tecnologias'})

# --- COMPETÊNCIAS ---
@login_required
def nova_competencia_view(request):
    if not e_gestor(request.user):
        return redirect('competencias')
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/form_competencia.html', {'form': form, 'acao': 'Adicionar'})

@login_required
def editar_competencia_view(request, id):
    if not e_gestor(request.user):
        return redirect('competencias')
    competencia = Competencia.objects.get(id=id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/form_competencia.html', {'form': form, 'acao': 'Editar'})

@login_required
def apagar_competencia_view(request, id):
    if not e_gestor(request.user):
        return redirect('competencias')
    competencia = Competencia.objects.get(id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/apagar_generico.html', {'item': competencia, 'tipo': 'Competência', 'url_cancelar': 'competencias'})

# --- LICENCIATURAS ---
@login_required
def nova_licenciatura_view(request):
    if not e_gestor(request.user):
        return redirect('licenciaturas')
    if request.method == 'POST':
        form = LicenciaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('licenciaturas')
    else:
        form = LicenciaturaForm()
    return render(request, 'portfolio/form_licenciatura.html', {'form': form, 'acao': 'Adicionar'})

@login_required
def editar_licenciatura_view(request, id):
    if not e_gestor(request.user):
        return redirect('licenciaturas')
    licenciatura = Licenciatura.objects.get(id=id)
    if request.method == 'POST':
        form = LicenciaturaForm(request.POST, instance=licenciatura)
        if form.is_valid():
            form.save()
            return redirect('licenciaturas')
    else:
        form = LicenciaturaForm(instance=licenciatura)
    return render(request, 'portfolio/form_licenciatura.html', {'form': form, 'acao': 'Editar'})

@login_required
def apagar_licenciatura_view(request, id):
    if not e_gestor(request.user):
        return redirect('licenciaturas')
    licenciatura = Licenciatura.objects.get(id=id)
    if request.method == 'POST':
        licenciatura.delete()
        return redirect('licenciaturas')
    return render(request, 'portfolio/apagar_generico.html', {'item': licenciatura, 'tipo': 'Licenciatura', 'url_cancelar': 'licenciaturas'})