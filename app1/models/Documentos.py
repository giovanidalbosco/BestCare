from app1.models import *


class Documentos(models.Model):
    documentoCreate = models.DateTimeField(verbose_name='TimeStamp', auto_now_add=True, blank=True)
    documento_pessoa_nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name='Residente', default='')
    documento_nome = models.CharField(max_length=50, verbose_name='Documentos', default='')
    documento_arquivo = models.FileField(verbose_name='Upload', default='')


    def __str__(self):
        return f'{self.documento_pessoa_nome} : {self.documento_nome}'

    
    class Meta:
        ordering = ['documento_pessoa_nome']
        verbose_name = 'Documento'