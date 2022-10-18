from app1.views import *


@login_required
def SinalVital_edit(request, id):
    sinalVital = get_object_or_404(SinalVital, pk=id)
    form = SinalVitalForm(instance=sinalVital)
    if (request.method == 'POST'):
        form = SinalVitalForm(request.POST, instance=sinalVital)
        if (form.is_valid()):
            sinalVital.save()
            return redirect('/sinalvital_list')
        else:
            return render(request, 'sinalvital_form.html', {
                'form': form, 
                'sinalvital': sinalVital
            })
    else:
        return render(request, 'sinalvital_form.html', {
            'form': form,
            'sinalVital': sinalVital
        })

