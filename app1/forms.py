from django import forms

from .models import Pessoas, Comorbidades, Uso_Consumo, Estoque_Individual, Ocorrencias, Prescricao

class Cadastro(forms.ModelForm):

    class Meta:
        model = Pessoas

        fields = ('pessoa_nome','pessoa_CPF','pessoa_email',)


class Uso_ConsumoForm(forms.ModelForm):

    class Meta:
        model = Uso_Consumo
        fields = ('consumo_nome', 'consumo_fabricante', 'consumo_apresentacao', 'consumo_via',)

class Estoque_IndividualForm(forms.ModelForm):

    class Meta:
        model = Estoque_Individual
        fields = ('estoque_pessoa_nome','estoque_usos_consumo','estoque_quantidade',)


class OcorrenciasForm(forms.ModelForm):

    class Meta:
        model = Ocorrencias
        fields = ('ocorrencia_nome', 'ocorrencia_pessoa_nome', 'ocorrencia_pessoa_cuidador', 'ocorrencia_observacao',)


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
            'pessoa_plano',
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
            'pessoa_email',
        )


class ResponsavelForm(forms.ModelForm):

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
            'pessoa_email',
        )


class PrescricaoForm(forms.ModelForm):

    class Meta:
        model = Prescricao
        fields = (
            'prescricao_pessoa_nome',
            'prescricao_consumo_nome',
            'prescricao_frequencia',
            'prescricao_aprazamento',
            'prescricao_dose',
            'prescricao_inicio',
            'prescricao_fim',
            'prescricao_observacao',
        )
