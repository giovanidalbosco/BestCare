from app1.models import *


class Event(models.Model):
    title = models.CharField(max_length=200)
    prescricao_pessoa_nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Residente", default='')
    prescricao_consumo_nome = models.ForeignKey(Uso_Consumo, on_delete=models.CASCADE, verbose_name="Produto", default='')
    prescricao_frequencia = models.IntegerField(choices=FREQUENCIA, default='')
    prescricao_dose = models.IntegerField(choices=DOSE, default='')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
