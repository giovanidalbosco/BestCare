from app1.views import *


@login_required
def Estoque_Individual_add(request):
    if request.method == 'POST':
        form = Estoque_IndividualForm(request.POST)
        print(f'testando {form}')
        if form.is_valid():
            estoque_Individual = form.save(commit=False)
            estoque_Individual.save()
            print(f'salvo {estoque_Individual}')
            return HttpResponseRedirect('/estoque_individual_list')
            # return redirect('/estoque_individual_list')
    else:
        # meu_objeto = Pessoas.objects.filter(pessoa_nome__icontains='Samir').first()
        # meu_objeto = get_object_or_404(Estoque_Individual, pk=1)
        meu_objeto = Estoque_Individual.objects.filter(estoque_pessoa_nome__pessoa_nome='Samir').first()
        print(meu_objeto)
        form = Estoque_IndividualForm(instance=meu_objeto)

        # form = Estoque_IndividualForm()

        

    return render(request, 'estoque_individual_add.html', {'form': form})