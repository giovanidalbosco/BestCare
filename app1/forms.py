from django import forms
from .models import Pessoas, Comorbidades, Uso_Consumo, Estoque_Individual, Ocorrencias

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
        fields = ('consumo_nome', 'consumo_fabricante', 'consumo_apresentacao', 'consumo_via',)

class Estoque_IndividualForm(forms.ModelForm):

    class Meta:
        model = Estoque_Individual
        fields = ('estoque_pessoa_nome','estoque_usos_consumo',)


class OcorrenciasForm(forms.ModelForm):

    class Meta:
        model = Ocorrencias
        fields = ('ocorrencia_nome', 'ocorrencia_pessoa_nome', 'ocorrencia_pessoa_cuidador',)


class ResidentesForm(forms.ModelForm):

    class Meta:
        model = Pessoas
        fields = (
            'pessoa_nome', 
            'pessoa_endereco', 
            'pessoa_numero',
            'pessoa_compl',
            'pessoa_cidade',
            'pessoa_classe',
            'pessoa_CPF',
            'pessoa_comorbidade',
            'pessoa_plano'
        )


class CuidadoresForm(forms.ModelForm):

    class Meta:
        model = Pessoas
        fields = (
            'pessoa_nome', 
            'pessoa_endereco', 
            'pessoa_numero',
            'pessoa_compl',
            'pessoa_cidade',
            'pessoa_classe',
            'pessoa_CPF',
            'pessoa_telefone',
            'pessoa_email'
        )
