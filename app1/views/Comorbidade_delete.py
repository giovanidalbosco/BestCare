from app1.views import *


@login_required
def Comorbidade_delete(request, id):
    comorbidades = get_object_or_404(Comorbidades, pk=id)
    comorbidades.delete()
    messages.info(request, 'Comorbidade apagada do banco de dados')
    return redirect('/comorbidades_list')