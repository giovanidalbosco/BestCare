from app1.views import *


@login_required
def Responsavel_edit(request, id):
    responsavel = get_object_or_404(Pessoas, pk=id)
    form = ResponsavelForm(instance=responsavel)
    if (request.method == 'POST'):
        form = ResponsavelForm(request.POST, instance=responsavel)
        if (form.is_valid()):
            responsavel.save()
            return redirect('/responsavel_list')
        else:
            return render(request, 'responsavel_form.html', {
                'form': form, 
                 'responsavel': responsavel
             })
    else:
        return render(request, 'responsavel_form.html', {
            'form': form,
            'responsavel': responsavel
        })