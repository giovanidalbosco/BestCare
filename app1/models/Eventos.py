from app1.models import *


class Eventos(models.Model):
    eventoCreate = models.DateTimeField(verbose_name='TimeStamp', auto_now_add=True, blank=True)
    evento_pessoa_nome = models.ForeignKey(Pessoas, verbose_name='Residente', on_delete=models.CASCADE, default='')
    evento_observacao = models.CharField(max_length=100, verbose_name='Observacao', default='')


    def __str__(self):
        return f'{self.eventoCreate} : {self.evento_pessoa_nome} - {self.evento_observacao}'


    class Meta:
        ordering = ['evento_pessoa_nome']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'