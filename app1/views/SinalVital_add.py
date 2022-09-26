from app1.views import *


@login_required
def SinalVital_add(request):
    if request.method == 'POST':
        form = SinalVitalForm(request.POST)
        if form.is_valid():
            nova_sinalvital = form.save(commit=False)
            nova_sinalvital.save()
            return HttpResponseRedirect('/sinalVital_list')
        else:
            return render(request, 'sinalVital_form.html', {
                'form': form, 
                'sinalVital': sinalvital
            })
    else:
        form = SinalVitalForm()

    sinalvital = SinalVital.objects.all()

    return render(request, 'sinalVital_form.html', {'form': form,
    'sinalVital': sinalvital})