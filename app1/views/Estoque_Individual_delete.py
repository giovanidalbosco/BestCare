from app1.views import *


@login_required
def Estoque_Individual_delete(request, id):
    estoque_individual = get_object_or_404(Estoque_Individual, pk=id)
    estoque_individual.delete()
    messages.info(request, 'Estoque individual apagado do banco de dados')
    
    return redirect(f'/estoque_individual_list/?search={estoque_individual.estoque_pessoa_nome.pessoa_nome}')