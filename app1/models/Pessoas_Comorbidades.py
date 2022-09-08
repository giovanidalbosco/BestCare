from app1.models import *


class Pessoas_Comorbidades(models.Model):
    pessoa_comorbidade_nome = models.CharField(max_length=10, verbose_name='Nome', default=0) 