from app1.models import *


class Comorbidades(models.Model):
    comorbidade_nome = models.CharField(max_length=50, verbose_name='Comorbidade', default='')


    def __str__(self):
        return self.comorbidade_nome
        
    class Meta:
        ordering = ['comorbidade_nome']
        verbose_name = 'Comorbidade'
        verbose_name_plural = 'Comorbidades'