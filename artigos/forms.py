from django import forms
from .models import Artigo, Comentario

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        # O autor e os likes não entram no form porque são preenchidos automaticamente
        fields = ['titulo', 'texto', 'fotografia', 'link_externo'] 

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {'texto': ''} # Esconde a label para ficar mais minimalista
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreve aqui o teu comentário...'}),
        }