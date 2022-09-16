from app1.views import *


@login_required
def Residentes_edit(request, id):
    residente = get_object_or_404(Pessoas, pk=id)
    form = Uso_ConsumoForm(instance=residente)
    if (request.method == 'POST'):
        form = ResidentesForm(request.POST, instance=residente)
        if (form.is_valid()):
            residente.save()
            return redirect('/residentes_list')
        else:
            return render(request, 'residentes_edit.html', {
                'form': form, 
                 'residente': residente
             })
    else:
        return render(request, 'residentes_edit.html', {
            'form': form,
            'residente': residente
        })