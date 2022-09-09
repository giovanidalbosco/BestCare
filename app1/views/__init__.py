from http.client import ImproperConnectionState
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app1.models import *
from app1.forms import Cadastro, ComorbidadesForm, Uso_ConsumoForm
from django.http import HttpResponseRedirect
from django.contrib import messages

from .Agenda import Agenda
from .Cad import Cad
from .Comorbidade_delete import Comorbidade_delete
from .Comorbidade_edit import Comorbidade_edit
from .Comorbidades_add import Comorbidades_add
from .Comorbidades_list import Comorbidades_list
from .index import index
from .Inicial import Inicial
from .Solucoes import Solucoes
from .Somos import Somos
from .Uso_Consumo_delete import Uso_Consumo_delete
from .Uso_Consumo_edit import Uso_Consumo_edit
from .Uso_Consumo_add import Uso_Consumo_add
from .Uso_Consumo_list import Uso_Consumo_list