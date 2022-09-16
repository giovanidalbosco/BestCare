from app1.views import *


@login_required
def Ocorrencias_add(request):
    if request.method == 'POST':
        form = OcorrenciasForm(request.POST)
        if form.is_valid():
            nova_ocorrencia = form.save(commit=False)
            nova_ocorrencia.ocorrencia_nome = form.cleaned_data['ocorrencia_nome']
            nova_ocorrencia.ocorrencia_pessoa_nome = form.cleaned_data['ocorrencia_pessoa_nome']
            nova_ocorrencia.ocorrencia_pessoa_cuidador = form.cleaned_data['ocorrencia_pessoa_cuidador']
            nova_ocorrencia.save()
            return HttpResponseRedirect('/ocorrencias_list')
    else:
        form = OcorrenciasForm()

    ocorrencia = Ocorrencias.objects.all()

    return render(request, 'ocorrencias_add.html', {'form': form,
    'ocorrencias': ocorrencia})

