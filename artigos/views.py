from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

# Função auxiliar para verificar se pertence ao grupo "autores"
def e_autor(user):
    return user.groups.filter(name='autores').exists()

# Listagem de todos os artigos (Público)
def artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

# Ver um artigo específico e os seus comentários
def artigo_detalhe_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    # Lógica para adicionar comentário
    if request.method == 'POST':
        # Só utilizadores autenticados podem comentar
        if not request.user.is_authenticated:
            return redirect('login')
            
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user # O autor do comentário é o user logado
            comentario.save()
            return redirect('artigo_detalhe', id=artigo.id)
    else:
        form = ComentarioForm()
        
    return render(request, 'artigos/artigo_detalhe.html', {'artigo': artigo, 'comentarios': comentarios, 'form': form})

# Criar um artigo
@login_required
def novo_artigo_view(request):
    # Só o grupo "autores" pode criar
    if not e_autor(request.user):
        return redirect('artigos')
        
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user # Associa o artigo automaticamente a quem o está a criar
            artigo.save()
            return redirect('artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/form_artigo.html', {'form': form, 'acao': 'Criar Artigo'})

# Editar um artigo
@login_required
def editar_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    
    # REGRA: O utilizador só pode editar se for o autor deste artigo específico
    if request.user != artigo.autor:
        return redirect('artigos')
        
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigo_detalhe', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/form_artigo.html', {'form': form, 'acao': 'Editar Artigo'})

# Apagar um artigo
@login_required
def apagar_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if request.user != artigo.autor:
        return redirect('artigos')
        
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos')
    return render(request, 'artigos/apagar_artigo.html', {'artigo': artigo})

# Dar Like num artigo (Qualquer pessoa)
def like_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    artigo.likes += 1
    artigo.save()
    return redirect('artigo_detalhe', id=artigo.id)