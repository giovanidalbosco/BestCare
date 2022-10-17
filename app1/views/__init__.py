from http.client import ImproperConnectionState
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app1.models import *
from app1.forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

from .Base_telainicial import Base_telainicial
from .Agenda import *
from .Cadastro import Cadastro
from .Login import Login

from .Comorbidades_delete import Comorbidades_delete
from .Comorbidades_edit import Comorbidades_edit
from .Comorbidades_add import Comorbidades_add
from .Comorbidades_list import Comorbidades_list

from .index import index
from .Inicial import Inicial
from .Solucoes import Solucoes
from .Somos import Somos
from .Medicamentos_delete import Medicamentos_delete
from .Medicamentos_edit import Medicamentos_edit
from .Medicamentos_add import Medicamentos_add
from .Medicamentos_list import Medicamentos_list

from .Estoque_Individual_delete import Estoque_Individual_delete
from .Estoque_Individual_edit import Estoque_Individual_edit
from .Estoque_Individual_list import Estoque_Individual_list
from .Estoque_Individual_add import Estoque_Individual_add
from .Ocorrencias_list import Ocorrencias_list
from .Ocorrencias_add import Ocorrencias_add
from .Ocorrencias_edit import Ocorrencias_edit
from .Ocorrencias_delete import Ocorrencias_delete
from .Envia_email import envia_email
from .Residentes_list import Residentes_list
from .Residentes_add import Residentes_add
from .Residentes_edit import Residentes_edit
from .Residentes_delete import Residentes_delete
from .Cuidadores_list import Cuidadores_list
from .Cuidadores_add import Cuidadores_add
from .Cuidadores_edit import Cuidadores_edit
from .Cuidadores_delete import Cuidadores_delete
from .Responsavel_list import Responsavel_list
from .Responsavel_add import Responsavel_add
from .Responsavel_edit import Responsavel_edit
from .Responsavel_delete import Responsavel_delete
from .SinalVital_list import SinalVital_list
from .SinalVital_add import SinalVital_add
from .SinalVital_edit import SinalVital_edit
from .SinalVital_delete import SinalVital_delete
