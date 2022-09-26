from app1.views import *


@login_required
def Ocorrencias_add(request):
    if request.method == 'POST':
        form = OcorrenciasForm(request.POST)
        if form.is_valid():
            nova_ocorrencia = form.save(commit=False)
            nova_ocorrencia.save()
            return HttpResponseRedirect('/ocorrencias_list')
        else:
            return render(request, 'ocorrencias_form.html', {
                'form': form, 
                'ocorrencia': ocorrencia
            })
    else:
        form = OcorrenciasForm()

    ocorrencia = Ocorrencias.objects.all()

    return render(request, 'ocorrencias_form.html', {'form': form,
    'ocorrencia': ocorrencia})

