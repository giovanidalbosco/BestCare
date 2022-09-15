from app1.models import *


class Pessoas(models.Model): 
    pessoa_nome = models.CharField(max_length=50, verbose_name='Nome', default='')
    pessoa_endereco = models.CharField(max_length=100, verbose_name='Endereco', default='')
    pessoa_numero = models.CharField(max_length=10, verbose_name='Numero', default='')
    pessoa_compl = models.CharField(max_length=30, verbose_name='Complemento', default='')
    pessoa_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, verbose_name='Cidade', default='')
    pessoa_CPF = models.CharField(max_length=11, verbose_name='CPF', default=0)
    pessoa_classe = models.CharField(max_length=1, choices=CLASSE, default='')
    pessoa_telefone  = models.CharField(max_length=20, verbose_name='Telefone', default=0)
    pessoa_email = models.EmailField(verbose_name='E-mail', default='')
    pessoa_comorbidade = models.ManyToManyField(Comorbidades,verbose_name='Comorbidades')
    pessoa_plano = models.CharField(max_length=1, choices=PLANO, default='')



    def __str__(self):
        return self.pessoa_nome
    
    class Meta:
        ordering = ['pessoa_nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'