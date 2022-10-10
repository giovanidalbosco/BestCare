from app1.views import *


@login_required
def Medicamentos_add(request):
    if request.method == 'POST':
        form = MedicamentosForm(request.POST)
        if form.is_valid():
            novo_medicamentos = form.save(commit=False)
            novo_medicamentos.save()
            return HttpResponseRedirect('/medicamentos_list')
    else:
        form = MedicamentosForm()


    return render(request, 'medicamentos_form.html', {'form': form})
    