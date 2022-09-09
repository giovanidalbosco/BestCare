from app1.models import *


class Prescricao(models.Model):
    prescricao_pessoa_nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Residente", default='')
    prescricao_consumo_nome = models.ForeignKey(Uso_Consumo, on_delete=models.CASCADE, verbose_name="Produto", default='')
    prescricao_frequencia = models.CharField(max_length=1, choices=FREQUENCIA, default='')
    prescricao_aprazamento = models.TimeField(verbose_name='Aprazamento', editable=True)
    prescricao_dose = models.CharField(max_length=1, choices=DOSE, default='')
    prescricao_inicio = models.DateField(max_length=10, verbose_name='Data Inicio', default='')
    prescricao_fim = models.DateField(max_length=10, verbose_name='Data Fim', default='')
    prescricao_observacao = models.CharField(max_length=200, verbose_name='Observacao', default='')


    def __str__(self):
        return self.consumo_nome

    class Meta:
        verbose_name = 'Prescricao'
        verbose_name_plural = 'Prescricoes'