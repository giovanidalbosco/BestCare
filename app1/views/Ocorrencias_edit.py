from app1.views import *


@login_required
def Ocorrencias_edit(request, id):
    ocorrencia = get_object_or_404(Ocorrencias, pk=id)
    form = OcorrenciasForm(instance=ocorrencia)
    if (request.method == 'POST'):
        form = OcorrenciasForm(request.POST, instance=ocorrencia)
        if (form.is_valid()):
            ocorrencia.save()
            return redirect('/ocorrencias_list')
        
        else:
            return render(request, 'ocorrencias_form.html', {
                'form': form, 
                'ocorrencia': ocorrencia
            })
    
    else:
        return render(request, 'ocorrencias_form.html', {
            'form': form,
            'ocorrencia': ocorrencia
        })