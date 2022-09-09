from app1.models import *


class Estoque_Individual(models.Model):
    estoqueCreate = models.DateTimeField(verbose_name="TimeStamp",auto_now_add=True,blank=True)
    estoque_pessoa_nome = models.OneToOneField(Pessoas, on_delete=models.CASCADE, verbose_name='Residente', default='')
    estoque_usos_consumo = models.OneToOneField(Usos_Consumo, on_delete=models.CASCADE, verbose_name='Produto', default='')
    estoque_movimento = models.CharField(max_length=1, choices=Entrada_Saida, default='')
    estoque_quantidade = models.IntegerField(verbose_name='Quantidade', default=0)
    estoque_saldo = models.IntegerField(verbose_name='Saldo em Estoque', default=0)
# Calcular o saldo en estoque (estoque anterior + entrada - saida = saldo atual)


    def __str__(self):
        return f'{self.estoque_residente} : {self.estoque_usos_e_consumo} - {self.estoque_saldo}'

    class Meta:
        ordering = ['estoque_pessoa_nome']
        verbose_name = 'Estoque Individual'
        verbose_name_plural = 'Estoque Individuais'