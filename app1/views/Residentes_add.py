from app1.views import *


@login_required
def Residentes_add(request):
    if request.method == 'POST':
        form = ResidentesForm(request.POST)
        if form.is_valid():
            novo_residente = form.save(commit=False)
            novo_residente.save()
            return HttpResponseRedirect('/residentes_list')
    else:
        form = ResidentesForm()

    residente = Pessoas.objects.all()

    return render(request, 'residentes_add.html', {'form': form,
    'residentes': residente})