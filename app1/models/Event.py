from app1.models import *


class Event(models.Model):
    title = models.IntegerField(choices=EVENTO, default='', verbose_name= 'Evento')
    event_pessoa_nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Residente", default='')
    event_consumo_nome = models.ForeignKey(Medicamentos, on_delete=models.CASCADE, verbose_name='Medicamento', default='')
    event_dose = models.IntegerField(choices=DOSE, default=0, verbose_name='Dose')
    description = models.TextField(verbose_name='Descricao')
    start_time = models.DateTimeField(verbose_name='Dia/Hora - Inicio')
    end_time = models.DateTimeField(verbose_name='Dia/Hora - Fim')

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.get_title_display()} </a>'
