from app1.models import *


class Cidades(models.Model):
    cidade_nome = models.CharField(max_length=100, verbose_name='Cidade', default='')
    cidade_uf = models.CharField(max_length=2, verbose_name='UF', default='')


    def __str__(self):
        return f'{self.cidade_nome} - {self.cidade_uf}'
    
    class Meta:
        ordering = ['cidade_nome']
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'