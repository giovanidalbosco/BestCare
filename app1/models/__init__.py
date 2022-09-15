from django.db import models

CLASSE = (
        ('1', 'Cuidador'),
        ('2', 'Residente'),
        ('3','Responsavel')
    )
PLANO = (
        ('1','PARTICULAR'),
        ('2', 'SUS'),
        ('3', 'CONVENIO')
    )
APRESENTACAO = (
        ('1','Comprimido'),
        ('2','Dragea'),
        ('3', 'Gota'),
        ('4', 'Injetavel'),
        ('5', 'Ampola'),
        ('6', 'Bisnaga'),
        ('7', 'Unidade')
    )
VIA = (
        ('1','Oral'),
        ('2', 'Intra-Venoso'),
        ('3', 'Nasal'),
        ('4', 'Ocular')
    )

Entrada_Saida = (
        ('1', 'Entrada'),
        ('2', 'Saida')
    )

OCORRENCIAS = (
        ('1', 'Disturbio'),
        ('2', 'Queda'),
        ('3', 'Fisioterapia'),
        ('4', 'Consulta Medica'),
        ('5', 'Refeicao'),
        ('6', 'Quimioterapia'),
        ('7', 'Outros')
    )

FREQUENCIA = (
        ('1', 'Horario'),
        ('2', 'Diario'),
        ('3', 'Semanal'),
        ('4', 'Mensal')
    )
DOSE = (
        ('1', '1/4'),
        ('2', '1/2'),
        ('3', '3/4'),
        ('4', '1'),
        ('5', '1 + 1/4'),
        ('6', '1 + 1/2'),
        ('7', '1 + 3/4')
    )


from .Comorbidades import Comorbidades
from .Cidades import Cidades
from .Uso_Consumo import Uso_Consumo
from .Pessoas import Pessoas
from .Estoque_Individual import Estoque_Individual
from .Pessoas_Comorbidades import Pessoas_Comorbidades
from .Documentos import Documentos
from .Eventos import Eventos
from .Ocorrencias import Ocorrencias
from .Prescricao import Prescricao
from .SinalVital import SinalVital