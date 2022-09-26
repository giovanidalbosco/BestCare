from app1.views import *


@login_required
def SinalVital_edit(request, id):
    sinalvital = get_object_or_404(SinalVital, pk=id)
    form = SinalVitalForm(instance=sinalvital)
    if (request.method == 'POST'):
        form = SinalVitalForm(request.POST, instance=sinalvital)
        if (form.is_valid()):
            sinalvital.save()
            return redirect('/sinalvital_list')
        else:
            return render(request, 'sinalvital_form.html', {
                'form': form, 
                'sinalvital': sinalvital
            })
    else:
        return render(request, 'sinalvital_form.html', {
            'form': form,
            'ocorrencia': sinalvital
        })