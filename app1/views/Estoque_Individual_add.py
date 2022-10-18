from app1.views import *


@login_required
def Estoque_Individual_add(request, id):
    residente = get_object_or_404(Pessoas, id=id)
    if request.method == 'POST':
        form = Estoque_IndividualForm(request.POST)
        if form.is_valid():
            estoque_Individual = form.save(commit=False)
            estoque_Individual.estoque_pessoa_nome = residente
            estoque_Individual.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return HttpResponseRedirect(f'/estoque_individual_list/?search={residente.pessoa_nome}')
    else:
        form = Estoque_IndividualForm()
        
    return render(request, 'estoque_individual_form.html', {'form': form, 'residente': residente})