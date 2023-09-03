from app1.models import *
from django.core.validators import MaxValueValidator, MinValueValidator


class SinalVital(models.Model):
    sinalVitalCreate = models.DateTimeField(verbose_name='TimeStamp', auto_now_add=True, blank=True)
    sinalVital_pessoa_nome = models.ForeignKey(Pessoas, verbose_name='Residente', on_delete=models.CASCADE)
    sinalVital_pas = models.IntegerField(verbose_name='P.A. Sistolica', default=0, validators=[MaxValueValidator(240), MinValueValidator(60)])
    sinalVital_pad = models.IntegerField(verbose_name='P.A. Diastolica', default=0, validators=[MaxValueValidator(160), MinValueValidator(40)])
    sinalVital_fc = models.IntegerField(verbose_name='Frequencia Cardiaca', default=0, validators=[MaxValueValidator(240), MinValueValidator(60)])
    sinalVital_fr = models.IntegerField(verbose_name='Frequencia Respiratoria', default=0, validators=[MaxValueValidator(100), MinValueValidator(12)])
    sinalVital_temp = models.FloatField(verbose_name='Temperatura', default=0, validators=[MaxValueValidator(43.0), MinValueValidator(33.0)])
    sinalVital_peso = models.FloatField(verbose_name='Peso', default=0)
    sinalVital_altura = models.FloatField(verbose_name='Altura', default=0)
    sinalVital_IMC = models.FloatField(verbose_name='IMC', default=0)

    def __str__(self):
        return f'{self.sinalVitalCreate} : {self.sinalVital_pessoa_nome} PAS: {self.sinalVital_pas}  PAD: {self.sinalVital_pad}'

    class Meta:
        ordering = ['-sinalVitalCreate']
        verbose_name = 'Sinal Vital'
        verbose_name_plural = 'Sinais Vitais'



