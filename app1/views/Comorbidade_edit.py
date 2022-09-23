from app1.views import *


@login_required
def Comorbidade_edit(request, id):
    comorbidades = get_object_or_404(Comorbidades, pk=id)
    form = ComorbidadesForm(instance=comorbidades)
    if (request.method == 'POST'):
        form = ComorbidadesForm(request.POST, instance=comorbidades)
        if (form.is_valid()):
            comorbidades.save()
            return redirect('/comorbidades_list')
        else:
            return render(request, 'comorbidade_form.html', {
                'form': form, 
                'comorbidade': comorbidades
            })
    else:
        return render(request, 'comorbidades_form.html', {
            'form': form,
            'comorbidade': comorbidades
        })