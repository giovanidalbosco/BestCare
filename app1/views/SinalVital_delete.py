from app1.views import *


@login_required
def SinalVital_delete(request, id):
    sinalvital = get_object_or_404(SinalVital, pk=id)
    sinalvital.delete()
    messages.info(request, 'Sinal Vital apagado do banco de dados')
    return redirect('/sinalVital_list')