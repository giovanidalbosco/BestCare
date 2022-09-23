from django.db import models

CLASSE = (
        (1, 'Cuidador'),
        (2, 'Residente'),
        (3,'Responsavel')
    )
PLANO = (
        (1,'PARTICULAR'),
        (2, 'SUS'),
        (3, 'CONVENIO')
    )
APRESENTACAO = (
        (1,'Comprimido'),
        (2,'Dragea'),
        (3, 'Gota'),
        (4, 'Injetavel'),
        (5, 'Ampola'),
        (6, 'Bisnaga'),
        (7, 'Unidade'),
        (8, 'Adesivo'),
        (9, 'Aerosol'),
        (10, 'Bolsa'),
        (11, 'Capsula'),
        (12, 'Colirio'),
        (13, 'Creme'),
        (14, 'Envelope'),
        (15, 'Inalatorio'),
        (16, 'Injetavel UI'),
        (17, 'Pilula'),
        (18, 'Pomada'),
        (19, 'Sache'),
        (20, 'Seringa'),
        (21, 'Shampoo'),
        (22, 'Solucao Gotas'),
        (23, 'Solucao ML'),
        (24, 'Solucao UI'),
        (25, 'Suspencao'),
        (26, 'Xarope'),
        (27, 'Tablete')
    )
VIA = (
        (1,'Oral'),
        (2, 'Intra-Venoso'),
        (3, 'Nasal'),
        (4, 'Ocular'),
        (5, 'Intramuscular'),
        (6, 'Topico'),
        (7, 'Nebulizacao'),
        (8, 'Otologica'),
        (9, 'Retal'),
        (10, 'Sonda-Nasoenteral'),
        (11, 'Gastrostomia'),
        (12, 'Sub-cutanea'),
        (13, 'Sub-lingual'),
        (14, 'Vaginal'),
    )

Entrada_Saida = (
        (1, 'Entrada'),
        (2, 'Saida')
    )

OCORRENCIAS = (
        (1, 'Agressividade'),
        (2, 'Alteracoes Glicemia'),
        (3, 'Cefaleia'),
        (4, 'Convulcao'),
        (5, 'Cuidado Paliativo'),
        (6, 'Deficit Motor'),
        (7, 'Desidratacao'),
        (8, 'Desnutricao'),
        (9, 'Diarreia'),
        (10 ,'Doencas Respiratorias'),
        (11, 'Dor Abdominal'),
        (12, 'Dor Epigastrica'),
        (13, 'dor Torassica'),
        (14, 'Entorce'),
        (15, 'Escabiose'),
        (16, 'Febre'),
        (17, 'FR Alterada'),
        (18, 'Ematoma'),
        (19, 'Infeccao TRato Urinario'),
        (20, 'Internacao'),
        (21, 'Lesao de Pele'),
        (22, 'Liberacao de Cateteres e Sondas'),
        (23, 'Modificacao de Prescricao'),
        (24, 'Neutropenia Febril'),
        (25, 'Obito'),
        (26, 'PA Alterada'),
        (27, 'Queda'),
        (28, 'Retirada de Dispositivo')
    )

FREQUENCIA = (
        (1, 'Horario'),
        (2, 'Diario'),
        (3, 'Semanal'),
        (4, 'Mensal'),
        (5, 'Dias Alternados'),
        (6, 'Criterio Medico')
    )
DOSE = (
        (1, '1/4'),
        (2, '1/2'),
        (3, '3/4'),
        (4, '1'),
        (5, '1 + 1/4'),
        (6, '1 + 1/2'),
        (7, '1 + 3/4')
    )

COMORBIDADES = (
    (1, 'Asma em uso de corticoide inalatório ou sistêmico (Moderada ou Grave)'),
    (2, 'Doença Pulmonar Obstrutiva Crônica (DPOC)'),
    (3, 'Bronquiectasia'),
    (4, 'Fibrose Cística'),
    (5, 'Doenças Intersticiais do pulmão'),
    (6, 'Displasia broncopulmonar'),
    (7, 'Hipertensão Arterial Pulmonar'),
    (8, 'Doença cardíaca congênita'),
    (9, 'Hipertensão arterial sistêmica com comorbidade'),
    (10, 'Doença cardíaca isquêmica'), 
    (11, 'Insuficiência cardíaca'),
    (12, 'Doença renal nos estágios 3,4 e 5'),
    (13, 'Síndrome nefrótica'),
    (14, 'Paciente em diálise'),
    (15, 'Atresia biliar'),
    (16, 'Hepatites crônicas'),
    (17, 'Cirrose'),
    (18, 'função respiratória Comprometida'),
    (19, 'Acidente Vascular Cerebral'),
    (20, 'Indivíduos com paralisia cerebral'), 
    (21, 'Esclerose múltipla'),
    (22, 'Doenças hereditárias'),
    (23, 'Doencas Degenerativas'),
    (24, 'Deficiência neurológica grave'),
    (25, 'Diabetes Mellitus tipo I e tipo II'),
    (26, 'Imunodeficiência'),
    (27, 'Obesidade grau III'),
    (28, 'Síndrome de Down'),
    (29, 'Síndrome de Klinefelter'),
    (30, 'Síndrome de Wakany'),

)


from .Comorbidades import Comorbidades
from .Cidades import Cidades
from .Uso_Consumo import Uso_Consumo
from .Pessoas import Pessoas
from .Estoque_Individual import Estoque_Individual
from .Documentos import Documentos
from .Eventos import Eventos
from .Ocorrencias import Ocorrencias
from .Prescricao import Prescricao
from .SinalVital import SinalVital
from .Event import Event