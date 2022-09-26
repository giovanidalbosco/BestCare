from app1.views import *


@login_required
def Uso_Consumo_add(request):
    if request.method == 'POST':
        form = Uso_ConsumoForm(request.POST)
        if form.is_valid():
            novo_uso_consumo = form.save(commit=False)
            novo_uso_consumo.save()
            return HttpResponseRedirect('/uso_consumo_list')
    else:
        form = Uso_ConsumoForm()


    return render(request, 'uso_consumo_add.html', {'form': form})
    