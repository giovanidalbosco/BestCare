from app1.views import *


@login_required
def Comorbidades_add(request):
    if request.method == 'POST':
        form = ComorbidadesForm(request.POST)
        if form.is_valid():
            nova_comorbidade = form.save(commit=False)
            nova_comorbidade.save()
            return HttpResponseRedirect('/comorbidades_list')
    else:
        form = ComorbidadesForm()

    comorbidade = Comorbidades.objects.all()

    return render(request, 'comorbidades_form.html', {'form': form,
    'comorbidade': comorbidade})