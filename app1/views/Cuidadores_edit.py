from app1.views import *


@login_required
def Cuidadores_edit(request, id):
    cuidador = get_object_or_404(Pessoas, pk=id)
    form = CuidadoresForm(instance=cuidador)
    if (request.method == 'POST'):
        form = CuidadoresForm(request.POST, instance=cuidador)
        if (form.is_valid()):
            cuidador.save()
            return redirect('/cuidadores_list')
        else:
            return render(request, 'cuidadores_form.html', {
                'form': form, 
                 'cuidador': cuidador
             })
    else:
        return render(request, 'cuidadores_form.html', {
            'form': form,
            'cuidador': cuidador
        })