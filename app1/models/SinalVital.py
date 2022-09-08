from app1.models import *


class SinalVital(models.Model):
    sinalVitalCreate = models.DateTimeField(verbose_name='TimeStamp', auto_now_add=True, blank=True)
    sinalVital_pessoa_nome = models.ForeignKey(Pessoas, verbose_name='Residente', on_delete=models.CASCADE)
    sinalVital_pas = models.CharField(max_length=5, verbose_name='PAS', default='')
    sinalVital_pad = models.CharField(max_length=5, verbose_name='PAD', default='')
    sinalVital_fc = models.CharField(max_length=5, verbose_name='FC', default='')
    sinalVital_fr = models.CharField(max_length=5, verbose_name='FR', default='')
    sinalVital_temp = models.CharField(max_length=5, verbose_name='TEMP', default='')
    sinalVital_peso = models.IntegerField(verbose_name='Peso', default=0)
    sinalVital_altura = models.IntegerField(verbose_name='Altura', default=0)
    sinalVital_IMC = models.IntegerField(verbose_name='IMC', default=0)
# Calcular o IMC (peso / (Altura**2))


    def __str__(self):
        return f'{self.sinalVitalCreate} : {self.sinalVital_nome} PAS: {self.sinalVital_pas}  PAD: {self.sinalVital_pad}'

    class Meta:
        ordering = ['sinalVital_pessoa_nome']
        verbose_name = 'Sinal Vital'
        verbose_name_plural = 'Sinais Vitais'