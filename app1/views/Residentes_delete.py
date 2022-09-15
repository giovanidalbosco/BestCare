from app1.views import *


@login_required
def Residentes_delete(request, id):
    ocorrencia = get_object_or_404(Pessoas, pk=id)
    ocorrencia.delete()
    messages.info(request, 'Residente apagado do banco de dados')
    return redirect('/residentes_list')