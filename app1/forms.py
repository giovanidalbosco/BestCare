from django import forms
from .models import Pessoas, Comorbidades, Uso_Consumo

class Cadastro(forms.ModelForm):

    class Meta:
        model = Pessoas

        fields = ('pessoa_nome','pessoa_CPF','pessoa_email',)

class ComorbidadesForm(forms.ModelForm):

    class Meta:
        model = Comorbidades
        fields = ('comorbidade_nome',)

class Uso_ConsumoForm(forms.ModelForm):

    class Meta:
        model = Uso_Consumo
        fields = ('consumo_nome',)