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
        form = OcorrenciasForm()

    ocorrencia = Ocorrencias.objects.all()

    return render(request, 'ocorrencias_add.html', {'form': form,
    'ocorrencia': ocorrencia})

'''
@login_required
def pessoa_add(request, id=0):

    if request.method == 'POST':
        form = PessoasForm(request.POST)
        if form.is_valid():
            nova_pessoa = form.save(commit=False)
            nova_pessoa.pessoa_nome = form.cleaned_data['pessoa_nome']
            nova_pessoa.pessoa_idade = form.cleaned_data['pessoa_idade']
            nova_pessoa.save()
            return HttpResponseRedirect('/pessoas/list')
    else:
        form = PessoasForm()

    pessoas = Pessoas.objects.all()

    return render(request, 'pessoas/add.html',
                  {
                      'form': form,
                      'pessoas': pessoas
                  }

                  )
'''