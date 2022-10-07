from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Pessoas)
admin.site.register(Cidades)
admin.site.register(Estoque_Individual)
admin.site.register(Eventos)
admin.site.register(Comorbidades)
admin.site.register(Uso_Consumo)
admin.site.register(SinalVital)
admin.site.register(Prescricao)
admin.site.register(Ocorrencias)
admin.site.register(Event)



