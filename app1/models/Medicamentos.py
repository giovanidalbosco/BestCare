from app1.models import *


class Medicamentos(models.Model):
    medicamento_nome = models.CharField(max_length=50, verbose_name='Uso e consumo', default='')
    medicamento_fabricante = models.CharField(max_length=50, verbose_name='Fabricante', default='')
    medicamento_apresentacao = models.IntegerField(verbose_name='Apresentacao', choices=APRESENTACAO, default=None)
    medicamento_via = models.IntegerField(choices=VIA, default=None)

    def __str__(self):
        return self.medicamento_nome

    class Meta:
        ordering = ['medicamento_nome']
        verbose_name = 'Medicamentos'