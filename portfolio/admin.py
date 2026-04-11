from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular, Tecnologia

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao", "ano_inicio", "ano_conclusao",)
    ordering = ("nome", "ano_inicio",)
    search_fields = ("nome", "instituicao",)

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_curricular", "semestre", "ects", "licenciatura",)
    ordering = ("ano_curricular", "semestre", "nome",)
    search_fields = ("nome", "docente_nome",)
    list_filter = ("ano_curricular", "semestre", "licenciatura",) # Mantive os filtros porque o enunciado pede explicitamente para os usar

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel_interesse", "link_oficial",)
    ordering = ("-nivel_interesse", "nome",) # O sinal de menos ordena do interesse mais alto para o mais baixo
    search_fields = ("nome",)

admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)