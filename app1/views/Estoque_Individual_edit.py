from app1.views import *


@login_required
def Estoque_Individual_edit(request, id):
    estoque_individual = get_object_or_404(Estoque_Individual, pk=id)
    residente = get_object_or_404(Pessoas, pk=estoque_individual.estoque_pessoa_nome.id)
    form = Estoque_IndividualForm(instance=estoque_individual)
    if (request.method == 'POST'):
        form = Estoque_IndividualForm(request.POST, instance=estoque_individual)
        if (form.is_valid()):
            estoque_individual = form.save(commit=False)
            estoque_individual.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            
            return redirect(f'/estoque_individual_list/?search={estoque_individual.estoque_pessoa_nome.pessoa_nome}')
        
        else:
            return render(request, 'estoque_individual_form.html', {
                'form': form, 
                'estoque_individual': estoque_individual
            })
    
    else:
        return render(request, 'estoque_individual_form.html', {
            'form': form,
            'estoque_individual': estoque_individual,
            'residente': residente
        })