from django.shortcuts import render
from .models import Curso, Professor, Aluno

def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professores_view(request):
    # Prefetch para ir buscar os cursos de cada professor de forma eficiente
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola/professores.html', {'professores': professores})

def alunos_view(request):
    # Prefetch para ir buscar os cursos de cada aluno de forma eficiente
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})