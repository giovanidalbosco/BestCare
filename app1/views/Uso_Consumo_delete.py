from app1.views import *


@login_required
def Uso_Consumo_delete(request, id):
    uso_consumo = get_object_or_404(Uso_Consumo, pk=id)
    uso_consumo.delete()
    messages.info(request, 'Uso/consumo apagado do banco de dados')
    return redirect('/uso_consumo_list')