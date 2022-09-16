from app1.views import *


@login_required
def Residentes_add(request):
    if request.method == 'POST':
        form = ResidentesForm(request.POST)
        if form.is_valid():
            novo_residente = form.save(commit=False)
            novo_residente.pessoa_nome = form.cleaned_data['pessoa_nome']
            novo_residente.pessoa_endereco = form.cleaned_data['pessoa_endereco']
            novo_residente.pessoa_numero = form.cleaned_data['pessoa_numero']
            novo_residente.pessoa_compl = form.cleaned_data['pessoa_compl']
            novo_residente.pessoa_cidade = form.cleaned_data['pessoa_cidade']
            novo_residente.pessoa_CPF = form.cleaned_data['pessoa_CPF']
            novo_residente.pessoa_comorbidade = form.cleaned_data['pessoa_comorbidade']
            novo_residente.pessoa_plano = form.cleaned_data['pessoa_plano']
            novo_residente.save()
            return HttpResponseRedirect('/residentes_list')
    else:
        form = ResidentesForm()

    residente = Pessoas.objects.all()

    return render(request, 'residentes_add.html', {'form': form,
    'residentes': residente})