from django import forms
from django.forms import ModelForm, DateInput

from .models import *

<<<<<<< HEAD
=======
from .models import Pessoas, Uso_Consumo, Estoque_Individual, Ocorrencias, Prescricao, Comorbidades
>>>>>>> 7f82b47009b2cc34d1591922405cb83d4846e2ac

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



class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
