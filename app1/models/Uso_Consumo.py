from app1.models import *


class Uso_Consumo(models.Model):
    consumo_nome = models.CharField(max_length=50, verbose_name='Uso e consumo', default='')
    consumo_fabricante = models.CharField(max_length=50, verbose_name='Fabricante', default='')
    consumo_apresentacao = models.CharField(max_length=1, verbose_name='Apresentacao',choices=APRESENTACAO, default='')
    consumo_via = models.CharField(max_length=1, choices=VIA, default='')


    def __str__(self):
        return self.consumo_nome

    class Meta:
        ordering = ['consumo_nome']
        verbose_name = 'Uso e consumo'