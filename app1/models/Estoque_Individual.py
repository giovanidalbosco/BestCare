from app1.models import *


class Estoque_Individual(models.Model):
    estoqueCreate = models.DateTimeField(verbose_name="TimeStamp",auto_now_add=True,blank=True)
    estoque_pessoa_nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name='Residente')
    estoque_usos_consumo = models.ManyToManyField(Uso_Consumo, verbose_name='Produto')
    estoque_movimento = models.CharField(max_length=1, choices=Entrada_Saida, default='')
    estoque_quantidade = models.IntegerField(verbose_name='Quantidade', default=0)
    estoque_saldo = models.IntegerField(verbose_name='Saldo em Estoque', default=0)
# Calcular o saldo en estoque (estoque anterior + entrada - saida = saldo atual)


    def __str__(self):
        itens = ''
        for i in self.estoque_usos_consumo.all():
            itens += i.consumo_nome

        return f'{self.estoque_pessoa_nome.pessoa_nome}, {itens}'


    class Meta:
        verbose_name = 'Estoque Individual'
        verbose_name_plural = 'Estoque Individuais'