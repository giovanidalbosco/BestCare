from dataclasses import fields
from django import forms
from .models import Pessoas, Comorbidades

class Cadastro(forms.ModelForm):

    class Meta:
        model = Pessoas

        fields = ('pessoa_nome','pessoa_CPF','pessoa_email',)

class ComorbidadesForm(forms.ModelForm):

    class Meta:
        model = Comorbidades
        fields = ('comorbidade_nome',)