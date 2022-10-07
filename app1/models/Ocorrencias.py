from app1.models import *


class Ocorrencias(models.Model):
    ocorrencia_nome = models.IntegerField(choices=OCORRENCIAS, verbose_name='Ocorrencia', default='')
    ocorrencia_pessoa_nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE,verbose_name='Residente')
    ocorrencia_pessoa_cuidador = models.ForeignKey(Pessoas, on_delete=models.CASCADE,verbose_name='Cuidador', related_name='+')
    ocorrencia_observacao = models.TextField(verbose_name='Observação', blank=True)


    def __str__(self):
        return f'{self.ocorrencia_nome} - Residente: {self.ocorrencia_pessoa_nome} Cuidador: {self.ocorrencia_pessoa_cuidador}'
    
    
    class Meta:
        verbose_name = 'Ocorrencia'
        verbose_name_plural = 'Ocorrencias'