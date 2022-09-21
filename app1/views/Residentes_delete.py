from app1.views import *


@login_required
def Residentes_delete(request, id):
    residente = get_object_or_404(Pessoas, pk=id)
    residente.delete()
    messages.info(request, 'Residente apagado do banco de dados')
    return redirect('/residentes_list')