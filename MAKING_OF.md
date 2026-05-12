# 🛠️ Making Of - Diário de Bordo Completo (Ficha 6 e Ficha 8)

**Autor:** Diego Nascimento  
**Número:** a22403352  
**Unidade Curricular:** Programação Web  

---

## 1. 📝 Modelação e Planeamento Inicial
O desenvolvimento do portfólio começou com uma fase de rascunho em papel. O objetivo foi definir a estrutura de dados antes de tocar em qualquer linha de código.
* **Diagrama Entidade-Relacionamento (DER):** Identifiquei as entidades principais e as suas relações (ex: um Projeto pode ter várias Tecnologias, e uma Unidade Curricular pertence a uma Licenciatura).

![Diagrama DER](/media/makingof/diagrama_der.jpeg) 

## 2. 🏗️ Arquitetura e Controlo de Versões
Diferente de exercícios anteriores, tomei a decisão estratégica de:
1. **Repositório Limpo:** Criar um novo repositório Git e um projeto Django do zero para garantir que não existia lixo residual de bases de dados de fichas passadas.
2. **Commits Granulares:** Seguir uma lógica de commits incrementais, separando a criação dos modelos da configuração do admin e dos scripts de automação.

## 3. 🛠️ Implementação Técnica e Resolução de Problemas
Durante o processo, surgiram desafios técnicos que permitiram aprofundar o conhecimento no ecossistema Django:

### 📸 O Erro do Pillow
Ao adicionar campos de imagem (`ImageField`), o Django emitiu um erro crítico indicando a falta de suporte para processamento de imagem.
* **Resolução:** Instalação da biblioteca `Pillow` via pip, permitindo a gestão correta de logótipos e capturas de ecrã diretamente para a diretoria `/media/`.

### 🔌 Integração com API (Fase 5)
Foi desenvolvido um script (`import_api.py`) para consumir dados da API da Lusófona via pedido POST. Devido a limitações de conectividade/timeout com o servidor externo durante os testes em ambiente cloud, a estratégia foi adaptada: utilizei os modelos criados para popular as Unidades Curriculares essenciais manualmente via Django Admin, garantindo o cumprimento dos objetivos da Ficha.

## 4. 🤖 Automação e Gestão de Dados (TFCs)
O ponto mais complexo do projeto foi o script `load_tfcs.py`. 
O dataset original em JSON continha trabalhos misturados de 2024 e 2025. Para cumprir o guião, implementei uma lógica de filtragem em Python antes da inserção na base de dados SQLite:

```python
# Excerto da lógica de filtragem implementada
for item in dados:
    ano_info = item.get('licenciaturas', '')
    
    # Ignora os trabalhos que não sejam da edição de 2025
    if '2025' not in ano_info:
        continue
        
    TFC.objects.create(...)
```

## 5. 📝 Ficha 8: Desvendando o Poder dos Formulários
Nesta etapa, o objetivo foi criar páginas que permitissem gerir os conteúdos da aplicação através de operações CRUD (Create, Read, Update, Delete).

### 🛠️ Implementação de CRUD e ModelForms
Implementei formulários para as classes de Projetos, Tecnologias, Competências e Formação.
* **Dificuldades:** A gestão de ficheiros media em formulários de edição foi desafiante, exigindo o uso de `request.FILES` no backend e `enctype="multipart/form-data"` no frontend.
* **Vantagens do Django:** A utilização de `ModelForms` provou ser extremamente vantajosa, permitindo gerar interfaces de entrada de dados seguras e validadas com poucas linhas de código.

## 6. 📄 Modelação Avançada e Tecnologias
Conforme solicitado, aprimorei a classe `Tecnologia` para incluir uma descrição detalhada e uma categorização por tipos.
* **Nova Classe TipoTecnologia:** Criei esta classe para estruturar as tecnologias em categorias como Frontend, Backend, Base de Dados, entre outras.
* **Reflexão Técnica:** Esta alteração permitiu uma organização mais semântica do portfólio, facilitando a navegação do utilizador e a gestão administrativa dos dados.

## 7. ✨ Página "Sobre" e Markdownify
Criei uma página técnica dedicada a explicar a arquitetura MVT do Django e a modelação da aplicação.
* **Markdownify:** Integrei este módulo para converter este diário de bordo de Markdown para HTML automaticamente, garantindo que a formatação original fosse mantida sem necessidade de duplicar esforço de escrita.

## 8. 🎥 Vídeo-Tutorial e Demonstração
Gravei um vídeo-tutorial explicando detalhadamente os passos para a construção da página de criação de novos projetos, abordando desde o `models.py` até ao template HTML final. O vídeo demonstra o funcionamento da rota, a lógica da view e a interação com a base de dados.

## 9. 🐙 Repositório GitHub
O uso do GitHub foi essencial para manter o controlo de versões granulado. Esta tecnologia trouxe vantagens como a rastreabilidade das alterações e a facilidade de colaboração em ambiente de desenvolvimento cloud.