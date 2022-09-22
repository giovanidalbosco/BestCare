from app1.views import *


@login_required
def Cuidadores_add(request):
    if request.method == 'POST':
        form = CuidadoresForm(request.POST)
        if form.is_valid():
            novo_cuidador = form.save(commit=False)
            novo_cuidador.save()
            return HttpResponseRedirect('/cuidadores_list')
    else:
        form = CuidadoresForm()

    cuidador = Pessoas.objects.all()

    return render(request, 'cuidadores_add.html', {'form': form,
    'cuidadores': cuidador})