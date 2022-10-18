from app1.models import *


class SinalVital(models.Model):
    sinalVitalCreate = models.DateTimeField(verbose_name='TimeStamp', auto_now_add=True, blank=True)
    sinalVital_pessoa_nome = models.ForeignKey(Pessoas, verbose_name='Residente', on_delete=models.CASCADE)
    sinalVital_pas = models.CharField(max_length=5, verbose_name='P.A. Sistolica', default='')
    sinalVital_pad = models.CharField(max_length=5, verbose_name='P.A. Diastolica', default='')
    sinalVital_fc = models.CharField(max_length=5, verbose_name='Frequencia Cardiaca', default='')
    sinalVital_fr = models.CharField(max_length=5, verbose_name='Frequencia Respiratoria', default='')
    sinalVital_temp = models.CharField(max_length=5, verbose_name='Temperatura', default='')
    sinalVital_peso = models.FloatField(verbose_name='Peso', default=0)
    sinalVital_altura = models.FloatField(verbose_name='Altura', default=0)
    sinalVital_IMC = models.FloatField(verbose_name='IMC', default=0)

    def __str__(self):
        return f'{self.sinalVitalCreate} : {self.sinalVital_pessoa_nome} PAS: {self.sinalVital_pas}  PAD: {self.sinalVital_pad}'

    class Meta:
        ordering = ['-sinalVitalCreate']
        verbose_name = 'Sinal Vital'
        verbose_name_plural = 'Sinais Vitais'



