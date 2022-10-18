from app1.views import *


@login_required
def Responsavel_delete(request, id):
    responsavel = get_object_or_404(Pessoas, pk=id)
    responsavel.delete()
    messages.info(request, 'Responsavel apagado do banco de dados')
    
    return redirect('/responsavel_list')