from app1.views import *


@login_required
def Uso_Consumo_list(request):
    search = request.GET.get('search')
    if search:
        uso_consumo = Uso_Consumo.objects.filter(consumo_nome__icontains=search)
    else:
        uso_consumo = Uso_Consumo.objects.all()


    return render(request, 'uso_consumo_list.html', {'uso_consumo': uso_consumo})
