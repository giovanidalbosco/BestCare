from app1.models import *


class Uso_Consumo(models.Model):
    consumo_nome = models.CharField(max_length=50, verbose_name='Uso e consumo', default='')
    consumo_fabricante = models.CharField(max_length=50, verbose_name='Fabricante', default='')
    consumo_apresentacao = models.IntegerField(verbose_name='Apresentacao', choices=APRESENTACAO, default=None)
    consumo_via = models.IntegerField(choices=VIA, default=None)


    def __str__(self):
        return self.consumo_nome

    class Meta:
        ordering = ['consumo_nome']
        verbose_name = 'Uso e consumo'