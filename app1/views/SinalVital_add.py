from app1.views import *


@login_required
def SinalVital_add(request):
    if request.method == 'POST':
        form = SinalVitalForm(request.POST)
        if form.is_valid():
            nova_sinalvital = form.save(commit=False)
            nova_sinalvital.save()
            return HttpResponseRedirect('/sinalvital_list')
        else:
            return render(request, 'sinalvital_form.html', {
                'form': form
            })
    else:
        form = SinalVitalForm()


    return render(request, 'sinalvital_form.html', {'form': form})
