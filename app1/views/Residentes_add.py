from app1.views import *


@login_required
def Residentes_add(request):
    if request.method == 'POST':
        form = ResidentesForm(request.POST)
        if form.is_valid():
            novo_residente = form.save(commit=False)
            novo_residente.pessoa_classe = '2'
            novo_residente.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return HttpResponseRedirect('/residentes_list')
    
    else:
        form = ResidentesForm()

    residente = Pessoas.objects.all()

    return render(request, 'residentes_form.html', {'form': form, 'residente': residente})
