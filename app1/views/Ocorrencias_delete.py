from app1.views import *


@login_required
def Ocorrencias_delete(request, id):
    ocorrencia = get_object_or_404(Ocorrencias, pk=id)
    ocorrencia.delete()
    messages.info(request, 'Ocorrencia apagada do banco de dados')
    return redirect('/ocorrencias_list')