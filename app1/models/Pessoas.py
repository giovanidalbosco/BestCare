from io import open_code
from random import choices
from app1.models import *


class Pessoas(models.Model): 
    pessoa_nome = models.CharField(max_length=50, verbose_name='Nome', null=False, blank=False, unique=True)
    pessoa_endereco = models.CharField(max_length=100, verbose_name='Endereco', blank=True, null=True)
    pessoa_numero = models.CharField(max_length=10, verbose_name='Numero', blank=True, null=True)
    pessoa_compl = models.CharField(max_length=30, verbose_name='Complemento', blank=True, null=True)
    pessoa_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name='Cidade', default='')
    pessoa_CPF = models.CharField(max_length=11, verbose_name='CPF', default=0, unique=True)
    pessoa_classe = models.IntegerField(choices=CLASSE, blank=False, null=False)
    pessoa_telefone  = models.CharField(max_length=20, verbose_name='Telefone', blank=True, null=True, unique=True)
    pessoa_email = models.EmailField(verbose_name='E-mail', blank=True, null=True, unique=True)
    pessoa_comorbidade = models.ManyToManyField(Comorbidades, verbose_name='Comorbidades')
    pessoa_plano = models.IntegerField(choices=PLANO, blank=True, null=True)



    def __str__(self):
        return self.pessoa_nome
    
    
    class Meta:
        ordering = ['pessoa_nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'