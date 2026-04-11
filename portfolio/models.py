from django.db import models

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ano_inicio = models.IntegerField()
    ano_conclusao = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.instituicao}'

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/')
    docente_nome = models.CharField(max_length=100)
    docente_link = models.URLField()
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')

    def __str__(self):
        return f'{self.nome} ({self.ano_curricular}º Ano)'