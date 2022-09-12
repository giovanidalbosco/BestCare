from app1.views import *


@login_required
def Estoque_Individual_add(request):
    print('aqui 1')
    if request.method == 'POST':
        print('aqui 2')
        form = Estoque_IndividualForm(request.POST)
        if form.is_valid():
            print('aqui 3')
            estoque_Individual = form.save(commit=False)
            estoque_Individual.save()
            return render(request, 'estoque_individual_list.html')
    else:
        print('aqui 4')
        form = Estoque_IndividualForm()

    print('aqui 5')
    return render(request, 'estoque_individual_add.html', {'form': form})