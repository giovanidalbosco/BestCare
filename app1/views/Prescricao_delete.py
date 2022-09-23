from app1.views import *


@login_required
def Prescricao_delete(request, id):
    prescricao = get_object_or_404(Prescricao, pk=id)
    prescricao.delete()
    messages.info(request, 'Prescricao apagada do banco de dados')
    return redirect('/prescricao_list')