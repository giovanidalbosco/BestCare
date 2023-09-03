from app1.views import *


@login_required
def Medicamentos_delete(request, id):
    medicamentos = get_object_or_404(Medicamentos, pk=id)
    medicamentos.delete()
    messages.info(request, 'Medicamentos apagado do banco de dados')
    
    return redirect('/medicamentos_list')