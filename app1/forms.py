from django import forms
from .models import *


class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput, label='Usuario', required=True)
    senha = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Senha', required=True)

class CadastroForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput, label='Usuario', required=True)
    # endereco = forms.CharField(widget=forms.TextInput, label='Endereço', required=True)
    # numero = forms.CharField(widget=forms.TextInput, label='Número', required=True)
    # complemento = forms.CharField(widget=forms.TextInput, label='Complemento', required=True)
    # cidade = forms.CharField(widget=forms.TextInput, label='Cidade', required=True)
    # CPF = forms.CharField(widget=forms.TextInput, label='CPF', required=True)
    # telefone = forms.CharField(widget=forms.TextInput, label='Telefone', required=True)
    email = forms.CharField(widget=forms.EmailInput, required=True)
    senha = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Senha', required=True)

    class Meta:
        model = Pessoas
        fields = '__all__'
        exclude = ('pessoa_nome', 'pessoa_classe', 'pessoa_email', 'pessoa_comorbidade', 'pessoa_plano')

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
            'pessoa_CEP',
            'pessoa_classe',
            'pessoa_CPF',
            'pessoa_comorbidade',
            'pessoa_plano',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pessoa_CEP'].widget.attrs.update({'class': 'mask-cep'})
        self.fields['pessoa_CPF'].widget.attrs.update({'class': 'mask-cpf'})


class CuidadoresForm(forms.ModelForm):
    
    class Meta:
        model = Pessoas
        fields = (
            'pessoa_nome', 
            'pessoa_endereco', 
            'pessoa_numero',
            'pessoa_compl',
            'pessoa_cidade',
            'pessoa_CEP',
            'pessoa_classe',
            'pessoa_CPF',
            'pessoa_telefone',
            'pessoa_email',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pessoa_CEP'].widget.attrs.update({'class': 'mask-cep'})
        self.fields['pessoa_CPF'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['pessoa_telefone'].widget.attrs.update({'class': 'mask-telefone'})
        
             
class ResponsavelForm(forms.ModelForm):
    
    class Meta:
        model = Pessoas
        fields = (
            'pessoa_nome', 
            'pessoa_endereco', 
            'pessoa_numero',
            'pessoa_compl',
            'pessoa_cidade',
            'pessoa_CEP',
            'pessoa_classe',
            'pessoa_CPF',
            'pessoa_telefone',
            'pessoa_email',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pessoa_CEP'].widget.attrs.update({'class': 'mask-cep'})
        self.fields['pessoa_CPF'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['pessoa_telefone'].widget.attrs.update({'class': 'mask-telefone'})
        

class PrescricaoForm(forms.ModelForm):
    
    class Meta:
        model = Prescricao
        fields = (
            'prescricao_pessoa_nome',
            'prescricao_consumo_nome',
            'prescricao_aprazamento',
            'prescricao_dose',
            'prescricao_inicio',
            'prescricao_fim',
            'prescricao_observacao',
        )


class SinalVitalForm(forms.ModelForm):
    sinalVital_pessoa_nome = forms.ModelChoiceField(
        widget = forms.Select,
        queryset = Pessoas.objects.filter(pessoa_classe=2),
        label = 'Residente'
    )
    

    class Meta:
        model = SinalVital
        fields = (
            'sinalVital_pessoa_nome',
            'sinalVital_pas',
            'sinalVital_pad',
            'sinalVital_fc',
            'sinalVital_fr',
            'sinalVital_peso',
            'sinalVital_altura',
            'sinalVital_IMC',
        )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
        'start_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        'end_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

