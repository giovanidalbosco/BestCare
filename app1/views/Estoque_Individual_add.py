from app1.views import *


@login_required
def Estoque_Individual_add(request, nome):
    pessoa = get_object_or_404(Pessoas, pessoa_nome=nome)
    if request.method == 'POST':
        form = Estoque_IndividualForm(request.POST)
        if form.is_valid():
            estoque_Individual = form.save(commit=False)
            estoque_Individual.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return HttpResponseRedirect('/estoque_individual_list')
            # return redirect('/estoque_individual_list')
    else:
        # meu_objeto = Pessoas.objects.filter(pessoa_nome__icontains='Samir').first()
        # meu_objeto = get_object_or_404(Estoque_Individual, pk=1)
        meu_objeto = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome=pessoa).first()
        form = Estoque_IndividualForm(instance=meu_objeto)

        # form = Estoque_IndividualForm()

        

    return render(request, 'estoque_individual_form.html', {'form': form})