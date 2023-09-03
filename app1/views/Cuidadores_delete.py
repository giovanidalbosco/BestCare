from app1.views import *


@login_required
def Cuidadores_delete(request, id):
    cuidador = get_object_or_404(Pessoas, pk=id)
    cuidador.delete()
    messages.info(request, 'Cuidador apagado do banco de dados')
    return redirect('/cuidadores_list')