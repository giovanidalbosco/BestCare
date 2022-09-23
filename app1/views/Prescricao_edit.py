from app1.views import *


@login_required
def Prescricao_edit(request, id):
    prescricao = get_object_or_404(Prescricao, pk=id)
    form = PrescricaoForm(instance=prescricao)
    if (request.method == 'POST'):
        form = PrescricaoForm(request.POST, instance=prescricao)
        if (form.is_valid()):
            prescricao.save()
            return redirect('/prescricao_list')
        else:
            return render(request, 'prescricao_edit.html', {
                'form': form, 
                'prescricao': prescricao
            })
    else:
        return render(request, 'prescricao_form.html', {
            'form': form,
            'ocorrencia': prescricao
        })