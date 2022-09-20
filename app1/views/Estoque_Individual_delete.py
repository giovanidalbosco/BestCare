from app1.views import *


@login_required
def Estoque_Individual_delete(request, id):
    estoque_individual = get_object_or_404(Estoque_Individual, pk=id)
    estoque_individual.delete()
    messages.info(request, 'Uso/consumo apagado do estoque')
    
    # return redirect('/estoque_individual_list')


    pessoa_nome = Pessoas.objects.all()
    dono_estoque = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome__icontains='Samir')
    pessoa_selec = Pessoas.objects.filter(pessoa_nome__icontains='Samir').first()

    context = {
        'estoque_individual': dono_estoque,
        'pessoa_nome': pessoa_nome,
        'pessoa_selec': pessoa_selec,
    }

    # return render(request, template_name='estoque_individual_list.html', context=context)
    
    # return HttpResponseRedirect('/estoque_individual_list')

    return Estoque_Individual_list(request, id)