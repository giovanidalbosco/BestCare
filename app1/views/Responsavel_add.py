from app1.views import *


@login_required
def Responsavel_add(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            novo_responsavel = form.save(commit=False)
            novo_responsavel.save()
            return HttpResponseRedirect('/responsavel_list')
    else:
        form = ResponsavelForm()

    responsavel = Pessoas.objects.all()

    return render(request, 'responsavel_add.html', {'form': form,
    'responsavel': responsavel})