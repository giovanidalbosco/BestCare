from app1.models import *


class Pessoas(models.Model): 
    pessoa_nome = models.CharField(max_length=50, verbose_name='Nome', null=False, blank=False, unique=True)
    pessoa_endereco = models.CharField(max_length=100, verbose_name='Endereco', blank=True, null=True)
    pessoa_numero = models.CharField(max_length=10, verbose_name='Numero', blank=True, null=True)
    pessoa_compl = models.CharField(max_length=30, verbose_name='Complemento', blank=True, null=True)
    pessoa_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name='Cidade', default='')
    pessoa_CEP = models.CharField(max_length=10, verbose_name='CEP', blank=True, null=True)
    pessoa_CPF = models.CharField(max_length=14, verbose_name='CPF', unique=True)
    pessoa_classe = models.IntegerField(choices=CLASSE, blank=False, null=False)
    pessoa_telefone  = models.CharField(max_length=15, verbose_name='Telefone', blank=True, null=True, unique=True)
    pessoa_email = models.EmailField(verbose_name='E-mail', blank=True, null=True, unique=True)
    pessoa_comorbidade = models.ManyToManyField(Comorbidades, verbose_name='Comorbidades')
    pessoa_plano = models.IntegerField(choices=PLANO, blank=True, null=True)
    pessoa_responsavel = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Responsável', blank=True, null=True)

    def __str__(self):
        return self.pessoa_nome
      
    def cria_cuidador(self, nome, email):
        self.pessoa_nome = nome
        self.pessoa_email = email
        self.pessoa_classe = 1
        self.pessoa_cidade_id = '2'

    class Meta:
        ordering = ['pessoa_nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'