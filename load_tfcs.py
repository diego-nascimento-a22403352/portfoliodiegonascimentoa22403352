import os
import django
import json

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC

def carregar_tfcs():
    caminho_ficheiro = 'data/tfcs_deisi_2025.json'

    with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    # Limpar a tabela antes de inserir
    TFC.objects.all().delete()
    print("A limpar dados antigos...")

    contador = 0
    # Percorrer o JSON e criar um objeto apenas para os de 2025
    for item in dados:
        ano_info = item.get('licenciaturas', '')
        
        # Se não tiver '2025' no texto, salta para o próximo e ignora este
        if '2025' not in ano_info:
            continue

        TFC.objects.create(
            titulo=item.get('titulo', ''),
            autores=item.get('autores', ''),
            orientadores=item.get('orientadores', ''),
            licenciaturas=ano_info,
            sumario=item.get('sumario', ''),
            palavras_chave=item.get('palavras_chave', ''),
            areas=item.get('areas', ''),
            tecnologias_usadas=item.get('tecnologias_usadas', ''),
            imagem=item.get('imagem', ''),
            link_pdf=item.get('link_pdf', ''),
            rating=item.get('rating', 3)
        )
        contador += 1
    
    print(f"Sucesso! Foram filtrados e carregados {contador} TFCs (apenas de 2025) na base de dados.")

if __name__ == '__main__':
    carregar_tfcs()