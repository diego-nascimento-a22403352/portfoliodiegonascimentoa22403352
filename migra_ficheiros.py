import os
from django.core.files import File
from django.conf import settings

# Importar os teus modelos com imagens
from portfolio.models import Projeto, Tecnologia, UnidadeCurricular
from escola.models import Curso

print("A iniciar migração para o Cloudinary...")

# 1. Migrar imagens dos Projetos
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        # Construir o caminho local manualmente
        local_path = os.path.join(settings.MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Projeto: {obj}")

# 2. Migrar logotipos das Tecnologias
for obj in Tecnologia.objects.all():
    if obj.logotipo and obj.logotipo.name:
        local_path = os.path.join(settings.MEDIA_ROOT, obj.logotipo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logotipo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrada Tecnologia: {obj}")

# 3. Migrar imagens das Unidades Curriculares
for obj in UnidadeCurricular.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrada UC: {obj}")

# 4. Migrar imagens dos Cursos (App Escola)
for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Curso: {obj}")

print("Migração concluída com sucesso!")