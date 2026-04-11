import os
import django
import requests

# 1. Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

def importar_dados_lusofona():
    # Dados do curso (LEI - 260)
    course_code = 260
    school_year = "202526"
    url_course = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    
    payload = {
        'language': 'PT',
        'courseCode': course_code,
        'schoolYear': school_year
    }

    print(f"A contactar a API da Lusófona para o curso {course_code}...")
    
    try:
        response = requests.post(url_course, json=payload)
        response.raise_for_status()
        data = response.json()
        
        # 2. Criar ou obter a Licenciatura
        # O nome da instituição e curso vêm da API
        licenciatura, created = Licenciatura.objects.get_or_create(
            nome=data.get('courseName', 'Engenharia Informática'),
            defaults={
                'instituicao': 'Universidade Lusófona',
                'ano_inicio': 2024,  # Valores genéricos, podes ajustar no Admin
                'ano_conclusao': 2027
            }
        )
        
        if created:
            print(f"Licenciatura '{licenciatura.nome}' criada com sucesso!")
        else:
            print(f"A usar a Licenciatura existente: {licenciatura.nome}")

        # 3. Importar as Unidades Curriculares (courseFlatPlan)
        ucs_data = data.get('courseFlatPlan', [])
        print(f"Encontradas {len(ucs_data)} disciplinas. A importar...")

        count_created = 0
        for uc_item in ucs_data:
            # Criar a UC se ela não existir (pelo nome)
            uc, created = UnidadeCurricular.objects.get_or_create(
                nome=uc_item.get('curricularUnitName'),
                licenciatura=licenciatura,
                defaults={
                    'ano_curricular': uc_item.get('curricularYear', 1),
                    'semestre': uc_item.get('semester', 1),
                    'ects': uc_item.get('ects', 6),
                    'docente_nome': 'A definir', # A API principal não envia o nome do docente diretamente aqui
                    'docente_link': 'https://www.ulusofona.pt'
                }
            )
            if created:
                count_created += 1

        print(f"Concluído! {count_created} novas disciplinas adicionadas à base de dados.")

    except Exception as e:
        print(f"Erro ao importar dados: {e}")

if __name__ == '__main__':
    importar_dados_lusofona()